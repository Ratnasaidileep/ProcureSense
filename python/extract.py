"""
Extract Module
Responsible for reading the procurement dataset.
"""

from pathlib import Path
import pandas as pd


def extract_data(file_path: Path) -> pd.DataFrame:
    """
    Reads the procurement CSV file.

    Args:
        file_path (Path): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    print("📥 Extracting dataset...")

    df = pd.read_csv(file_path)

    print(f"✅ Dataset loaded successfully ({len(df)} rows)")

    return df