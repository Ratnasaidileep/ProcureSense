"""
Main ETL Pipeline
"""

from config import RAW_DATA_PATH
from extract import extract_data
from loader import load_raw_data
from validate import validate_data

def main():

    print("=" * 60)
    print("ProcureSense ETL Pipeline")
    print("=" * 60)

    # Extract
    df = extract_data(RAW_DATA_PATH)
    validate_data(df)
    # Load Raw Data
    load_raw_data(df)

    print("\n✅ ETL Stage 1 Completed Successfully!")


if __name__ == "__main__":
    main()