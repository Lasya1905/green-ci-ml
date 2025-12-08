import json
import glob
import pandas as pd
import os

reports_path = "eco_reports"
if not os.path.exists(reports_path):
    print(f"{reports_path} folder not found. Make sure you have downloaded artifact JSONs there.")
    exit(1)

data = []
files = sorted(glob.glob(os.path.join(reports_path, "*.json")))
if not files:
    print("No JSON files found in eco_reports/. Download workflow artifacts first.")
    exit(1)

for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            r = json.load(f)
            # adjust keys depending on Eco CI output structure
            energy = r.get("energy") or r.get("energy_kwh") or r.get("energy_kwh_estimate")
            co2 = r.get("co2") or r.get("co2_g") or r.get("co2_g_estimate")
            duration = r.get("duration") or r.get("duration_s") or r.get("runtime_seconds")
            data.append({
                "filename": os.path.basename(fpath),
                "energy_kWh": energy,
                "co2_g": co2,
                "duration_s": duration
            })
    except Exception as e:
        print(f"Failed to read {fpath}: {e}")

df = pd.DataFrame(data)
df = df.dropna(subset=["energy_kWh", "co2_g", "duration_s"])  # drop incomplete
df.to_csv("pipeline_data.csv", index=False)
print("✅ pipeline_data.csv created with", len(df), "rows")