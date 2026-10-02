from typing import Literal

import pandas as pd


def create_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = create_agg_feature(df, feature="Invoice", agg="nunique")

    df = create_agg_feature(df, feature="Quantity", agg="sum")

    df = create_agg_feature(df, feature="Amount", agg="sum")

    df = create_unique_products(df)

    df = create_agg_feature(df, agg="mean", feature="Quantity")

    df = create_agg_feature(df, agg="max", feature="Quantity")

    df = create_agg_feature(df, agg="min", feature="Quantity")

    df = create_agg_feature(df, agg="mean", feature="Price")

    df = create_agg_feature(df, agg="median", feature="Price")

    df = create_agg_feature(df, agg="std", feature="Price")

    df = create_avg_description_length(df)

    df = create_has_multi_description_products(df)

    df = create_is_first_purchase(df)

    return df


def create_agg_feature(
    df: pd.DataFrame,
    agg: Literal["sum", "nunique", "mean", "max", "min", "median", "std"],
    feature: str,
) -> pd.DataFrame:
    if agg in ["nunique", "sum"]:
        name = f"Total_{feature.title()}"
    else:
        name = f"{agg.title()}_{feature.title()}"

    df[name] = df.groupby("Customer_ID")[feature].transform(agg)

    return df


def create_unique_products(df: pd.DataFrame) -> pd.DataFrame:
    df["Unique_Products"] = df.groupby("Customer_ID")["StockCode"].transform("nunique")

    return df


def create_avg_description_length(df: pd.DataFrame) -> pd.DataFrame:
    description_length = df["Description"].str.len()

    df["Mean_Description_Length"] = description_length.groupby(
        df["Customer_ID"]
    ).transform("mean")

    return df


def create_has_multi_description_products(df: pd.DataFrame) -> pd.DataFrame:
    description_counts = df.groupby("StockCode")["Description"].nunique()

    multi_description_products = description_counts[description_counts > 1].index

    has_multi_descriptions = df["StockCode"].isin(multi_description_products)

    df["Has_Multi_Description_Products"] = (
        has_multi_descriptions.groupby(df["Customer_ID"]).transform("any").astype(int)
    )

    return df


def create_is_first_purchase(df: pd.DataFrame) -> pd.DataFrame:
    df["Is_First_Purchase"] = df["Total_Invoice"].map(lambda x: x == 1).astype(int)

    return df
