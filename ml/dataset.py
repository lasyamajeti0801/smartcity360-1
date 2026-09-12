"""
SmartCity360 - Municipal Civic Issue Dataset Generator & Preprocessor
Generates a realistic municipal civic issue training dataset for NLP category routing
and priority prediction.
"""

import os
import random
from pathlib import Path
from typing import List, Dict, Any
import pandas as pd

# Seed for reproducible deterministic training
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

ISSUE_TEMPLATES = [
    # Category: POTHOLE (ROADS)
    ("Deep pothole causing vehicle damage and traffic backup near {location}", "POTHOLE", "ROADS", "HIGH"),
    ("Asphalt crater in the center carriage lane of {location}", "POTHOLE", "ROADS", "HIGH"),
    ("Multiple road surface cracks and minor potholes appearing along {location}", "POTHOLE", "ROADS", "MEDIUM"),
    ("Severe pavement failure creating hazardous depression on {location}", "POTHOLE", "ROADS", "CRITICAL"),
    ("Small gravel depression on the shoulder of {location}", "POTHOLE", "ROADS", "LOW"),

    # Category: GARBAGE (SANITATION)
    ("Overflowing municipal garbage container attracting rodents near {location}", "GARBAGE", "SANITATION", "MEDIUM"),
    ("Illegal commercial construction waste dumping on vacant lot at {location}", "GARBAGE", "SANITATION", "MEDIUM"),
    ("Rotting organic waste pile emitting severe odor blocking sidewalk on {location}", "GARBAGE", "SANITATION", "HIGH"),
    ("Missed scheduled weekly garbage pickup for entire residential block at {location}", "GARBAGE", "SANITATION", "LOW"),
    ("Hazardous medical or chemical waste discarded near park at {location}", "GARBAGE", "SANITATION", "CRITICAL"),

    # Category: STREETLIGHT_OUT (ELECTRICAL)
    ("Cluster of 5 streetlights completely dark along pedestrian path on {location}", "STREETLIGHT_OUT", "ELECTRICAL", "MEDIUM"),
    ("Broken streetlight fixture hanging dangerously from pole on {location}", "STREETLIGHT_OUT", "ELECTRICAL", "HIGH"),
    ("Flickering LED streetlight pole outside residence at {location}", "STREETLIGHT_OUT", "ELECTRICAL", "LOW"),
    ("Total electrical blackout of road lighting grid across {location}", "STREETLIGHT_OUT", "ELECTRICAL", "CRITICAL"),
    ("Exposed electrical wiring at base of public light pole on {location}", "STREETLIGHT_OUT", "ELECTRICAL", "CRITICAL"),

    # Category: WATER_LEAK (WATER)
    ("Major drinking water pipeline burst flooding roadway at {location}", "WATER_LEAK", "WATER", "CRITICAL"),
    ("Continuous clean water leakage from municipal distribution valve on {location}", "WATER_LEAK", "WATER", "HIGH"),
    ("Low water pressure reported in apartment complex at {location}", "WATER_LEAK", "WATER", "MEDIUM"),
    ("Turbid and discolored municipal tap water reported in {location}", "WATER_LEAK", "WATER", "HIGH"),
    ("Minor seepage from underground pipe joint near sidewalk at {location}", "WATER_LEAK", "WATER", "LOW"),

    # Category: DRAINAGE_BLOCK (ROADS)
    ("Stormwater drain clogged with plastic debris causing street flooding on {location}", "DRAINAGE_BLOCK", "ROADS", "HIGH"),
    ("Missing storm drain manhole cover creating lethal fall hazard on {location}", "DRAINAGE_BLOCK", "ROADS", "CRITICAL"),
    ("Stagnant water accumulation from blocked roadside gutter at {location}", "DRAINAGE_BLOCK", "ROADS", "MEDIUM"),
    ("Drainage overflow entering basement parking during rain on {location}", "DRAINAGE_BLOCK", "ROADS", "HIGH"),

    # Category: TRAFFIC_SIGNAL (ELECTRICAL)
    ("Traffic signal lights completely off at major four-way junction on {location}", "TRAFFIC_SIGNAL", "ELECTRICAL", "CRITICAL"),
    ("Traffic signal stuck on red causing severe vehicular gridlock on {location}", "TRAFFIC_SIGNAL", "ELECTRICAL", "HIGH"),
    ("Pedestrian crossing button not functioning on {location}", "TRAFFIC_SIGNAL", "ELECTRICAL", "LOW"),
    ("Traffic light timing misconfigured causing unnecessary queue at {location}", "TRAFFIC_SIGNAL", "ELECTRICAL", "MEDIUM"),
]

LOCATIONS = [
    "MG Road Metro Station", "Commercial Street Gate 3", "Elm Avenue Sector 7",
    "Hospital Boulevard Ward 2", "Civic Center Plaza", "Justice Highway",
    "Market Square Ward 4", "Industrial Estate Road 12", "Green Valley Boulevard",
    "University North Campus", "Riverfront Promenade", "Tech Park Main Gate",
    "Subway Concourse West", "Central Bus Terminal", "Railway Station East Approach"
]

def generate_civic_dataset(num_samples: int = 1500) -> pd.DataFrame:
    """Generates synthetic labeled civic complaints dataset with realistic text descriptions."""
    records = []
    for _ in range(num_samples):
        template, category, department, priority = random.choice(ISSUE_TEMPLATES)
        location = random.choice(LOCATIONS)
        text = template.format(location=location)
        ward = random.randint(1, 10)
        
        # Add slight natural text variation
        if random.random() > 0.6:
            text = f"Urgent: {text}. Please dispatch inspection crew immediately."
        elif random.random() > 0.7:
            text = f"Citizen Report: {text} Reported by residents of Ward {ward}."

        records.append({
            "text": text,
            "category": category,
            "department": department,
            "priority": priority,
            "ward_number": ward
        })

    df = pd.DataFrame(records)
    return df

def main():
    data_dir = Path(__file__).resolve().parent.parent / "data" / "processed"
    data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = data_dir / "civic_complaints_training.csv"
    
    print(f"[INFO] Generating realistic synthetic municipal dataset (1,500 records)...")
    df = generate_civic_dataset(1500)
    df.to_csv(csv_path, index=False)
    print(f"[SUCCESS] Dataset generated and persisted to {csv_path}")
    print(f"Distribution by Category:\n{df['category'].value_counts()}")
    print(f"\nDistribution by Priority:\n{df['priority'].value_counts()}")

if __name__ == "__main__":
    main()
