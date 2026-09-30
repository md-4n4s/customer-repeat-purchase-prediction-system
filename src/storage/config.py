from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_CSV_DIR = BASE_DIR / "data" / "raw" / "online_retail_II.xlsx"

INPUT_DIR = BASE_DIR / "data" / "raw" / "database" / "retail.db"

CLEAN_CSV_DIR = BASE_DIR / "data" / "clean" / "clean.csv"

CLEAN_DB_DIR = BASE_DIR / "data" / "clean" / "database" / "clean.db"

CLEAN_WITH_TARGET_CSV_DIR = BASE_DIR / "data" / "clean" / "clean_with_target.csv"

CLEAN_WITH_TARGET_DB_DIR = BASE_DIR / "data" / "clean" / "database" / "clean_with_target.db"
