"""
Multi-Agent Analysis Pipeline.

Objective: Perform deeper, multi-dimensional analysis on the dataset to extract
collaboration metrics and insights, without cluttering the main ETL script.
Inputs: src/data/pizza_metrics.json
Outputs: src/data/advanced_collaboration_insights.json
"""

import pandas as pd
import numpy as np
import json
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_metrics(input_path: str, output_path: str) -> None:
    """Read the metrics data, process with pandas, and write insights."""
    np.random.seed(42)  # For reproducibility per data_analyst skill
    
    if not os.path.exists(input_path):
        logging.error(f"Input file {input_path} not found.")
        return
        
    # Read data
    df = pd.read_json(input_path)
    
    # Avoid SettingWithCopyWarning
    df_clean = df.copy()
    
    # 1. Industry-level collaboration profile
    # Average focus_hours, meeting_overhead, and pizza_party_index
    industry_profile = (
        df_clean.groupby('industry')
        .agg(
            avg_focus_hours=('focus_hours', 'mean'),
            avg_meeting_overhead=('meeting_overhead', 'mean'),
            avg_pizza_party_index=('pizza_party_index', 'mean')
        )
        .round(2)
        .reset_index()
    )
    
    # 2. Correlation matrix (using numeric columns)
    numeric_df = df_clean.select_dtypes(include=[np.number])
    correlations = numeric_df.corr().round(3).to_dict()
    
    # 3. Best setup by age group
    # Setup that maximizes focus_hours / meeting_overhead ratio
    df_clean.loc[:, 'focus_meeting_ratio'] = df_clean['focus_hours'] / df_clean['meeting_overhead'].replace(0, np.nan)
    
    # Find the top work setup category for each age group based on this ratio
    best_setup = (
        df_clean.groupby(['age_group', 'work_setup_category'])['focus_meeting_ratio']
        .mean()
        .reset_index()
        .sort_values('focus_meeting_ratio', ascending=False)
        .groupby('age_group')
        .head(1)
        .round(2)
    )
    
    # 4. Aggregate Burnout Risk Score
    if 'burnout_risk_score' in df_clean.columns:
        burnout_profile = (
            df_clean.groupby(['work_setup_category', 'industry'])['burnout_risk_score']
            .mean()
            .round(4)
            .reset_index()
        )
    else:
        burnout_profile = pd.DataFrame()
        
    # 5. Calculate "True Productive Hours"
    if 'interruption_frequency' in df_clean.columns and 'focus_hours' in df_clean.columns:
        # Penalty of 0.33 hours (20 mins) per interruption
        df_clean['true_productive_hours'] = (df_clean['focus_hours'] - (df_clean['interruption_frequency'] * 0.33)).clip(lower=0)
        true_productivity_profile = (
            df_clean.groupby('work_setup_category')['true_productive_hours']
            .mean()
            .round(2)
            .reset_index()
        )
    else:
        true_productivity_profile = pd.DataFrame()
    
    # Construct output dictionary
    insights = {
        "industry_profile": industry_profile.to_dict(orient="records"),
        "correlations": correlations,
        "best_setup_by_age": best_setup.to_dict(orient="records"),
        "burnout_risk_profile": burnout_profile.to_dict(orient="records"),
        "true_productivity_profile": true_productivity_profile.to_dict(orient="records")
    }
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(insights, f, indent=4)
        
    logging.info(f"Advanced insights saved to {output_path}")

if __name__ == "__main__":
    analyze_metrics("src/data/pizza_metrics.json", "src/data/advanced_collaboration_insights.json")
