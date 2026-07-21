"""
ETL Pipeline for Pizza Party Metrics.

This script implements an ETL (Extract, Transform, Load) pipeline that:
1. Fetches GitHub issue/PR resolution times for multiple repositories representing
   different organizational work setups ('Remote-First', 'Hybrid', 'Onsite-Heavy').
2. Computes distinct velocity proxies for each work setup category instead of a single global scalar.
3. Downloads and parses the Work From Home (WFH) Research dataset.
4. Computes the Pizza Party Index, focus hours, meeting overhead, and demographic metrics.
5. Saves the resulting metrics in JSON format for downstream application usage.
"""

import os
import json
import logging
import requests
import pandas as pd
from datetime import datetime
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set fixed random seed as per data_analyst skill constraints
np.random.seed(42)

# Top-level constants
GITHUB_ISSUES_URL_TEMPLATE = "https://api.github.com/repos/{repo}/issues?state=closed&per_page={limit}"
WFH_DATA_URL = "https://wfhresearch.com/wp-content/uploads/2026/07/WFHtimeseries_monthly.xlsx"

# Repositories representing distinct work setups / organizational styles
SETUP_REPOS = {
    'Remote-First': [
        'gitlabhq/gitlabhq',
        'pandas-dev/pandas',
        'automattic/wp-calypso',
        'hashicorp/terraform'
    ],
    'Hybrid': [
        'microsoft/vscode',
        'facebook/react',
        'flutter/flutter'
    ],
    'Onsite-Heavy': [
        'apache/kafka',
        'tensorflow/tensorflow',
        'oracle/graal'
    ]
}

# Fallback velocity proxies if network or rate limit errors occur
FALLBACK_VELOCITIES = {
    'Remote-First': 0.070,
    'Hybrid': 0.050,
    'Onsite-Heavy': 0.035
}

AGE_GROUPS = ['18-24', '25-34', '35-44', '45-54', '55+']
GENDERS = ['Male', 'Female', 'Non-binary', 'Other']


def fetch_github_velocity(repo="pandas-dev/pandas", limit=100):
    """
    Fetch recent closed issues from a single GitHub repository to calculate an average velocity proxy.
    Returns average issue/PR resolution velocity (1 / median closing hours).
    """
    logging.info(f"Fetching GitHub issue data for {repo}...")
    url = GITHUB_ISSUES_URL_TEMPLATE.format(repo=repo, limit=limit)
    
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if os.getenv('GITHUB_TOKEN'):
        headers['Authorization'] = f"token {os.getenv('GITHUB_TOKEN')}"

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            logging.warning(f"Failed to fetch GitHub data for {repo} (Status {response.status_code}). Using fallback.")
            return 0.05
            
        issues = response.json()
        closing_times = []
        for issue in issues:
            if issue.get('created_at') and issue.get('closed_at'):
                created = pd.to_datetime(issue['created_at'])
                closed = pd.to_datetime(issue['closed_at'])
                diff_hours = (closed - created).total_seconds() / 3600.0
                if 0.05 <= diff_hours <= 8760: # Valid resolution window (3 mins to 1 year)
                    closing_times.append(diff_hours)
        
        if not closing_times:
            return 0.05
            
        avg_closing_time = np.median(closing_times)
        velocity = 1.0 / avg_closing_time if avg_closing_time > 0 else 0.05
        logging.info(f"Calculated {repo} median closing time: {avg_closing_time:.2f} hours. Velocity proxy: {velocity:.4f}")
        return velocity
    except Exception as e:
        logging.warning(f"Network request error fetching {repo}: {e}. Using fallback velocity.")
        return 0.05


def fetch_work_setup_velocities(setup_repos=None, limit=50):
    """
    Fetch issue resolution times for multiple repositories grouped by work setup category
    ('Remote-First', 'Hybrid', 'Onsite-Heavy').
    Returns a dictionary mapping category names to distinct velocity proxies.
    """
    if setup_repos is None:
        setup_repos = SETUP_REPOS

    velocities = {}
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if os.getenv('GITHUB_TOKEN'):
        headers['Authorization'] = f"token {os.getenv('GITHUB_TOKEN')}"

    for category, repos in setup_repos.items():
        logging.info(f"Fetching GitHub metrics for work setup category '{category}' across repos: {repos}...")
        closing_times = []
        
        for repo in repos:
            url = GITHUB_ISSUES_URL_TEMPLATE.format(repo=repo, limit=limit)
            try:
                response = requests.get(url, headers=headers, timeout=15)
                if response.status_code == 200:
                    issues = response.json()
                    for issue in issues:
                        if issue.get('created_at') and issue.get('closed_at'):
                            created = pd.to_datetime(issue['created_at'])
                            closed = pd.to_datetime(issue['closed_at'])
                            diff_hours = (closed - created).total_seconds() / 3600.0
                            if 0.05 <= diff_hours <= 8760:
                                closing_times.append(diff_hours)
                else:
                    logging.warning(f"Status {response.status_code} fetching {repo}")
            except Exception as e:
                logging.warning(f"Error fetching {repo}: {e}")

        if closing_times:
            median_time = float(np.median(closing_times))
            velocity = 1.0 / median_time if median_time > 0 else FALLBACK_VELOCITIES.get(category, 0.05)
            logging.info(f"Category '{category}' median resolution time: {median_time:.2f}h -> Velocity proxy: {velocity:.4f}")
        else:
            velocity = FALLBACK_VELOCITIES.get(category, 0.05)
            logging.warning(f"No valid data returned for category '{category}'. Used fallback velocity {velocity:.4f}")
            
        velocities[category] = velocity

    return velocities


def download_wfh_data(filepath="wfh_data.xlsx"):
    """
    Download WFH Research dataset if it doesn't exist locally.
    """
    url = WFH_DATA_URL
    if not os.path.exists(filepath):
        logging.info("Downloading WFH dataset...")
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            with open(filepath, 'wb') as f:
                f.write(response.content)
            logging.info("Downloaded WFH dataset successfully.")
        except Exception as e:
            logging.error(f"Failed to download WFH dataset: {e}")
            raise
    else:
        logging.info("WFH dataset already exists. Skipping download.")
    return filepath


def process_data(wfh_filepath, github_velocities):
    """
    Process the WFH data and calculate the Pizza Party Index using distinct work setup velocity proxies.
    Returns DataFrame formatted with demographically breakdown records.
    """
    logging.info("Reading WFH data...")
    df = pd.read_excel(wfh_filepath, sheet_name='Work Arrangements by Industry')
    
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna(subset=['date'])
    latest_df = df.sort_values('date', ascending=False).iloc[0:1].copy()
    
    # Extract industries
    industries = []
    for col in latest_df.columns:
        if col.startswith('full_onsite_'):
            ind = col.replace('full_onsite_', '')
            if ind not in industries and not pd.isna(latest_df[col].iloc[0]):
                industries.append(ind)

    # Normalize github_velocities input
    if isinstance(github_velocities, (int, float)):
        # Scalar fallback
        github_velocities = {
            'Remote-First': float(github_velocities),
            'Hybrid': float(github_velocities) * 0.8,
            'Onsite-Heavy': float(github_velocities) * 0.6
        }
    elif not isinstance(github_velocities, dict):
        github_velocities = FALLBACK_VELOCITIES

    results = []
    base_focus_hours = 40.0
    categories = ['Remote-First', 'Hybrid', 'Onsite-Heavy']

    # Reset seed for deterministic demographic generation
    np.random.seed(42)

    for ind in sorted(industries):
        onsite_col = f'full_onsite_{ind}'
        hybrid_col = f'hybrid_{ind}'
        remote_col = f'full_remote_{ind}'
        
        onsite_pct = (latest_df[onsite_col].iloc[0] if onsite_col in latest_df.columns else 0.0) / 100.0
        hybrid_pct = (latest_df[hybrid_col].iloc[0] if hybrid_col in latest_df.columns else 0.0) / 100.0
        remote_pct = (latest_df[remote_col].iloc[0] if remote_col in latest_df.columns else 0.0) / 100.0
        
        total = onsite_pct + hybrid_pct + remote_pct
        if total > 0:
            probs = [remote_pct / total, hybrid_pct / total, onsite_pct / total]
        else:
            probs = [0.33, 0.33, 0.34]

        industry_title = ind.replace('_', ' ').title()
        
        for age in AGE_GROUPS:
            for gender in GENDERS:
                # Sample work setup category based on industry probabilities
                cat = np.random.choice(categories, p=probs)
                cat_vel = github_velocities.get(cat, FALLBACK_VELOCITIES.get(cat, 0.05))

                if cat == 'Remote-First':
                    cat_factor = 0.55 + (remote_pct * 0.2)
                    perks_factor = 0.2 + (onsite_pct * 0.3)
                elif cat == 'Hybrid':
                    cat_factor = 0.45 + (hybrid_pct * 0.15)
                    perks_factor = 0.5 + (onsite_pct * 0.4)
                else:  # Onsite-Heavy
                    cat_factor = 0.35 + (onsite_pct * 0.1)
                    perks_factor = 0.8 + (onsite_pct * 0.2)
                
                # Small deterministic demographic variation (+/- 5%)
                noise = np.random.uniform(-0.05, 0.05)
                focus_hours = base_focus_hours * (cat_factor + noise) * (1.0 + cat_vel)
                meeting_overhead = max(5.0, base_focus_hours - focus_hours)
                
                # Pizza Party Index: Ratio of performative perks to focus hours
                pizza_party_index = (perks_factor / max(focus_hours, 1.0)) * 100.0

                record = {
                    'industry': industry_title,
                    'work_setup_category': cat,
                    'work_setup': {
                        'onsite_pct': round(float(onsite_pct) * 100.0, 2),
                        'hybrid_pct': round(float(hybrid_pct) * 100.0, 2),
                        'remote_pct': round(float(remote_pct) * 100.0, 2)
                    },
                    'focus_hours': round(float(focus_hours), 2),
                    'meeting_overhead': round(float(meeting_overhead), 2),
                    'pizza_party_index': round(float(pizza_party_index), 2),
                    'age_group': age,
                    'gender': gender
                }
                results.append(record)
        
    final_df = pd.DataFrame(results)
    return final_df


def main():
    os.makedirs('src/data', exist_ok=True)
    
    # Step 1: Fetch distinct velocity proxies for work setup categories
    velocities = fetch_work_setup_velocities()
    logging.info(f"Work setup velocities calculated: {velocities}")

    # Step 2: Download/ensure WFH data
    wfh_file = download_wfh_data()
    
    # Step 3: Process data using multi-category velocities
    final_df = process_data(wfh_file, velocities)
    
    output_path = 'src/data/pizza_metrics.json'
    logging.info(f"Saving results to {output_path} ({len(final_df)} records)...")
    final_df.to_json(output_path, orient='records', indent=4)
    logging.info("ETL pipeline completed successfully.")


if __name__ == '__main__':
    main()

