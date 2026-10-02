import pandas as pd


def finalize_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(
        columns=[
            "Invoice",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "Price",
            "Amount",
            "Week_Day",
            "Hour",
            "Month",
        ]
    )

    df = df.drop_duplicates(subset="Customer_ID", keep="first")

    target = df.pop("Target")
    df["Target"] = target

    return df
