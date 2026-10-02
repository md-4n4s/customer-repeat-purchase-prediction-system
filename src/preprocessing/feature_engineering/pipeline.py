from src.storage.config import (
    CLEAN_WITH_TARGET_DB_DIR,
    FEATURES_CSV_DIR,
    FEATURES_DB_DIR,
)
from src.storage.data_io import load_data, save_data

from .combined_features import create_combined_features
from .customer_features import create_customer_features
from .date_time_features import create_date_time_features
from .finalize_features import finalize_features
from .product_features import create_product_features
from .transaction_features import create_transaction_features


def feature_engineering_pipeline() -> None:
    df = load_data(CLEAN_WITH_TARGET_DB_DIR, "InvoiceDate")

    df = create_combined_features(df)

    df = create_customer_features(df)

    df = create_product_features(df)

    df = create_transaction_features(df)

    df = create_date_time_features(df)

    df = finalize_features(df)

    save_data(df, FEATURES_DB_DIR)

    save_data(df, FEATURES_CSV_DIR)


if __name__ == "__main__":
    feature_engineering_pipeline()
