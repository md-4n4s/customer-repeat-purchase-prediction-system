import pandas as pd


def create_product_features(df: pd.DataFrame) -> pd.DataFrame:
    df = create_agg_feature_per_product(df, feature="Amount", agg="mean")

    df = create_repeat_product_ratio(df)

    df = create_top_product_ratio(df)

    return df


def create_agg_feature_per_product(
    df: pd.DataFrame, feature: str, agg: str
) -> pd.DataFrame:
    feature_per_product = df.groupby(["Customer_ID", "StockCode"])[feature].sum()

    agg_feature_per_product = feature_per_product.groupby("Customer_ID").agg(
        agg.lower()
    )

    df[f"{agg.title()}_{feature.title()}_Per_Product"] = df["Customer_ID"].map(
        agg_feature_per_product
    )

    return df


def create_repeat_product_ratio(df: pd.DataFrame) -> pd.DataFrame:
    product_purchases = df.groupby(["Customer_ID", "StockCode"])["Invoice"].nunique()

    repeat_products = product_purchases.groupby("Customer_ID").apply(
        lambda x: (x > 1).sum()
    )

    total_products = product_purchases.groupby("Customer_ID").size()

    ratio = repeat_products / total_products

    df["Repeat_Product_Ratio"] = df["Customer_ID"].map(ratio)

    return df


def create_top_product_ratio(df: pd.DataFrame) -> pd.DataFrame:
    product_purchases = df.groupby(["Customer_ID", "StockCode"])["Invoice"].nunique()

    top_products = product_purchases.groupby("Customer_ID").max()

    total_products = product_purchases.groupby("Customer_ID").sum()

    ratio = top_products / total_products

    df["Top_Product_Ratio"] = df["Customer_ID"].map(ratio)

    return df
