import sys
import os
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Add the project root to sys.path to import scripts.etl
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.etl import fetch_work_setup_velocities, download_wfh_data, process_data

app = FastAPI(title="Pizza Party Metrics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CACHE = {
    "data": None,
    "timestamp": 0
}
CACHE_TTL = 3600 * 12  # 12 hours

@app.get("/api/metrics")
def get_metrics():
    current_time = time.time()
    if CACHE["data"] is not None and (current_time - CACHE["timestamp"]) < CACHE_TTL:
        return CACHE["data"]

    # Run ETL
    velocities, vel_metadata = fetch_work_setup_velocities()
    wfh_file = download_wfh_data()
    final_df = process_data(wfh_file, velocities)
    
    data = final_df.to_dict(orient="records")
    
    result = {
        "metrics": data,
        "metadata": vel_metadata
    }
    
    CACHE["data"] = result
    CACHE["timestamp"] = current_time
    
    return result
