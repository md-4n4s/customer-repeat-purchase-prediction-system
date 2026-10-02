import pandas as pd


def create_transaction_features(df: pd.DataFrame) -> pd.DataFrame:
    df = create_agg_products_per_invoice(df)

    df = create_agg_products_per_invoice(df, unique=True)

    df = create_agg_products_per_invoice(df, unique=True, agg="median")

    df = create_agg_feature_per_invoice(df, "Quantity", "mean")

    df = create_agg_feature_per_invoice(df, "Amount", "mean")

    df = create_agg_feature_per_invoice(df, "Quantity", "median")

    df = create_agg_feature_per_invoice(df, "Amount", "median")

    df = create_agg_feature_per_invoice(df, "Quantity", "max")

    df = create_agg_feature_per_invoice(df, "Amount", "max")

    df = create_agg_feature_per_invoice(df, "Amount", "std")

    return df


def create_agg_products_per_invoice(
    df: pd.DataFrame, agg: str = "mean", unique: bool = False
) -> pd.DataFrame:
    if unique:
        func = "nunique"
        name = "Unique_Products"
    else:
        func = "count"
        name = "Products"

    products_per_invoice = df.groupby(["Customer_ID", "Invoice"])["StockCode"].agg(func)

    avg_products_per_invoice = products_per_invoice.groupby("Customer_ID").agg(
        agg.lower()
    )

    df[f"{agg.title()}_{name}_Per_Invoice"] = df["Customer_ID"].map(
        avg_products_per_invoice
    )

    return df


def create_agg_feature_per_invoice(
    df: pd.DataFrame, feature: str, agg: str
) -> pd.DataFrame:
    feature_per_invoice = df.groupby(["Customer_ID", "Invoice"])[feature].sum()

    agg_feature_per_invoice = feature_per_invoice.groupby("Customer_ID").agg(
        agg.lower()
    )

    df[f"{agg.title()}_{feature.title()}_Per_Invoice"] = df["Customer_ID"].map(
        agg_feature_per_invoice
    )

    return df
