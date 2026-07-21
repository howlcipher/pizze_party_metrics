"""
Unit tests for the ETL pipeline in scripts/etl.py.
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import pandas as pd
import numpy as np

from scripts.etl import (
    fetch_github_velocity,
    fetch_work_setup_velocities,
    download_wfh_data,
    process_data,
    FALLBACK_VELOCITIES,
    SETUP_REPOS
)


class TestETLPipeline(unittest.TestCase):

    @patch('scripts.etl.requests.get')
    def test_fetch_github_velocity_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'created_at': '2026-01-01T00:00:00Z', 'closed_at': '2026-01-01T10:00:00Z'},
            {'created_at': '2026-01-01T00:00:00Z', 'closed_at': '2026-01-01T20:00:00Z'}
        ]
        mock_get.return_value = mock_response

        velocity = fetch_github_velocity(repo="test/repo")
        # Median time is 15 hours -> velocity = 1/15 = 0.0667
        self.assertAlmostEqual(velocity, 1.0 / 15.0, places=3)

    @patch('scripts.etl.requests.get')
    def test_fetch_github_velocity_failure_fallback(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        velocity = fetch_github_velocity(repo="test/repo")
        self.assertEqual(velocity, 0.05)

    @patch('scripts.etl.requests.get')
    def test_fetch_work_setup_velocities(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'created_at': '2026-01-01T00:00:00Z', 'closed_at': '2026-01-01T05:00:00Z'}
        ]
        mock_get.return_value = mock_response

        custom_repos = {'Remote-First': ['test/repo1'], 'Hybrid': ['test/repo2']}
        velocities = fetch_work_setup_velocities(setup_repos=custom_repos)

        self.assertIn('Remote-First', velocities)
        self.assertIn('Hybrid', velocities)
        self.assertAlmostEqual(velocities['Remote-First'], 1.0 / 5.0, places=3)

    def test_process_data_structure(self):
        wfh_filepath = 'wfh_data.xlsx'
        if not os.path.exists(wfh_filepath):
            self.skipTest("wfh_data.xlsx not available for integration test")

        velocities = {
            'Remote-First': 0.07,
            'Hybrid': 0.05,
            'Onsite-Heavy': 0.03
        }

        df = process_data(wfh_filepath, velocities)

        # Check total records: 14 industries * 5 age_groups * 4 genders = 280
        self.assertEqual(len(df), 280)

        # Check expected columns
        expected_cols = {
            'industry', 'work_setup_category', 'work_setup',
            'focus_hours', 'meeting_overhead', 'pizza_party_index',
            'age_group', 'gender'
        }
        self.assertTrue(expected_cols.issubset(set(df.columns)))

        # Check setup categories
        setup_categories = set(df['work_setup_category'])
        self.assertEqual(setup_categories, {'Remote-First', 'Hybrid', 'Onsite-Heavy'})


if __name__ == '__main__':
    unittest.main()
