import json
import os

def update_readme():
    metrics_path = "src/data/pizza_metrics.json"
    readme_path = "README.md"
    
    if not os.path.exists(metrics_path):
        print(f"Metrics file {metrics_path} not found.")
        return

    with open(metrics_path, "r") as f:
        data = json.load(f)
        
    num_records = len(data)
    avg_ppi = sum(d.get("pizza_party_index", 0) for d in data) / num_records if num_records > 0 else 0
    avg_focus = sum(d.get("focus_hours", 0) for d in data) / num_records if num_records > 0 else 0
    avg_meeting = sum(d.get("meeting_overhead", 0) for d in data) / num_records if num_records > 0 else 0
    
    summary_text = (
        f"**Total Records Analyzed**: {num_records}<br>\n"
        f"**Average Pizza Party Index**: {avg_ppi:.2f}<br>\n"
        f"**Average Focus Hours**: {avg_focus:.2f}<br>\n"
        f"**Average Meeting Overhead**: {avg_meeting:.2f}\n"
    )
    
    with open(readme_path, "r") as f:
        content = f.read()
        
    start_marker = "<!-- METRICS_START -->"
    end_marker = "<!-- METRICS_END -->"
    
    if start_marker in content and end_marker in content:
        start_idx = content.find(start_marker) + len(start_marker)
        end_idx = content.find(end_marker)
        
        new_content = content[:start_idx] + "\n" + summary_text + content[end_idx:]
        
        with open(readme_path, "w") as f:
            f.write(new_content)
        print("README.md updated successfully.")
    else:
        print("Markers not found in README.md")

if __name__ == "__main__":
    update_readme()
