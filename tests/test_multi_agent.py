import os
import json
import tempfile
from scripts.multi_agent_analysis import analyze_metrics


def test_analyze_metrics():
    # Create sample data
    sample_data = [
        {
            "industry": "Tech",
            "work_setup_category": "Remote-First",
            "focus_hours": 30.0,
            "meeting_overhead": 10.0,
            "pizza_party_index": 1.5,
            "age_group": "25-34",
            "gender": "Female"
        },
        {
            "industry": "Finance",
            "work_setup_category": "Hybrid",
            "focus_hours": 20.0,
            "meeting_overhead": 20.0,
            "pizza_party_index": 4.5,
            "age_group": "25-34",
            "gender": "Male"
        }
    ]
    
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "test_input.json")
        output_path = os.path.join(tmpdir, "test_output.json")
        
        with open(input_path, 'w') as f:
            json.dump(sample_data, f)
            
        analyze_metrics(input_path, output_path)
        
        if not os.path.exists(output_path):
            raise AssertionError("Output file does not exist")
        
        with open(output_path, 'r') as f:
            insights = json.load(f)
            
        if "industry_profile" not in insights:
            raise AssertionError("industry_profile missing")
        if "correlations" not in insights:
            raise AssertionError("correlations missing")
        if "best_setup_by_age" not in insights:
            raise AssertionError("best_setup_by_age missing")
        
        # Verify industry profile
        tech_profile = next(item for item in insights["industry_profile"] if item["industry"] == "Tech")
        if tech_profile["avg_focus_hours"] != 30.0:
            raise AssertionError(f"Expected 30.0, got {tech_profile['avg_focus_hours']}")
