"""
ProcureSense Configuration
"""

from pathlib import Path

# ============================
# Project Paths
# ============================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "procurement_data.csv"

# ============================
# MySQL Configuration
# ============================

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1209",
    "database": "procuresense",
    "port": 3306
}