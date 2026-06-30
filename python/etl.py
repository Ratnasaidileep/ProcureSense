import pandas as pd

from pathlib import Path

from loader import load_raw_data

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "procurement_data.csv"

print("Reading CSV...")

df = pd.read_csv(DATA_PATH)

print(f"Rows Loaded : {len(df)}")

load_raw_data(df)

print("\nETL Step 1 Complete!")