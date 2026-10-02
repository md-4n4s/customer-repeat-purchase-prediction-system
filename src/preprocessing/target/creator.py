import pandas as pd

from src.storage.config import (
    CLEAN_DB_DIR,
    CLEAN_WITH_TARGET_CSV_DIR,
    CLEAN_WITH_TARGET_DB_DIR,
)
from src.storage.data_io import load_data, save_data


# ===============================
# ------- Target Creation -------
# ===============================
def create_target(df: pd.DataFrame) -> pd.DataFrame:
    # Define the cutoff date as 90 days before the last transaction date.
    cutoff_date = df["InvoiceDate"].max() - pd.Timedelta(days=90)

    # Use transactions before the cutoff date to create customer features.
    pre_cutoff = df[df["InvoiceDate"] < cutoff_date].copy()

    # Use transactions from the cutoff date onward to determine repeat purchases.
    post_cutoff = df[df["InvoiceDate"] >= cutoff_date]

    # Get customers who made at least one purchase during the target period.
    post_cutoff_customers = set(post_cutoff["Customer_ID"].unique())

    # Mark customers as 1 if they purchased again during the target period.
    pre_cutoff["Target"] = (
        pre_cutoff["Customer_ID"].isin(post_cutoff_customers).astype(int)
    )

    return pre_cutoff


def main():
    # Load the cleaned dataset and parse InvoiceDate as a datetime column.
    df = load_data(CLEAN_DB_DIR, "InvoiceDate")

    # Create the repeat-purchase target using a 90-day cutoff.
    df = create_target(df)

    # Save the dataset with the target to the cleaned database.
    save_data(df, CLEAN_WITH_TARGET_DB_DIR)

    # Save the dataset with the target as a CSV file.
    save_data(df, CLEAN_WITH_TARGET_CSV_DIR)


if __name__ == "__main__":
    main()
