from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_CSV_DIR = BASE_DIR / "data" / "raw" / "online_retail_II.xlsx"

DB_DIR = BASE_DIR / "data" / "database" / "retail.db"
