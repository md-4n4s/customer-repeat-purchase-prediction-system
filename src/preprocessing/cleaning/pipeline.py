from src.storage.config import CLEAN_CSV_DIR, CLEAN_DB_DIR, INPUT_DIR
from src.storage.data_io import load_data, save_data

from .cleaner import *
from .validator import validate


def preprocessing_pipeline() -> pd.DataFrame:
    """Load, clean, and validate the dataset."""
    df = load_data(INPUT_DIR)

    cleaned_data = clean_data(df)

    validate(cleaned_data)

    save_data(cleaned_data, CLEAN_CSV_DIR)

    save_data(cleaned_data, CLEAN_DB_DIR)

    return cleaned_data


if __name__ == "__main__":
    preprocessing_pipeline()
