"""
Validation Module
Performs data quality checks on the procurement dataset.
"""

import pandas as pd


REQUIRED_COLUMNS = [
    "tender_no.",
    "tender_description",
    "agency",
    "award_date",
    "tender_detail_status",
    "supplier_name",
    "awarded_amt"
]


def validate_data(df: pd.DataFrame) -> None:
    """
    Validate the input dataset before processing.

    Raises:
        ValueError: If required columns are missing.
    """

    print("\n🔍 Running data validation...")

    # Check required columns
    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("✅ Required columns present")

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate rows
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")

    # Negative contract values
    negative = (df["awarded_amt"] < 0).sum()
    print(f"Negative Contract Values: {negative}")

    print("\n✅ Validation completed successfully.")