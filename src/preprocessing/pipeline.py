from .cleaner import *
from .config import INPUT_DIR
from .loader import load_data
from .validator import validate


def preprocessing_pipeline() -> pd.DataFrame:
    """Load, clean, and validate the dataset."""
    df = load_data(INPUT_DIR)

    cleaned_data = clean_data(df)

    validate(cleaned_data)

    return cleaned_data


if __name__ == "__main__":
    preprocessing_pipeline()
