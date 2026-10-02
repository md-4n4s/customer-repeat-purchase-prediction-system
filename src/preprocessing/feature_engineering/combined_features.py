import pandas as pd


def create_combined_features(df: pd.DataFrame) -> pd.DataFrame:
    df = create_amount(df)

    df = modify_country(df)

    df = create_week_day(df)

    df = create_hour(df)

    df = create_month(df)

    df = create_date(df)

    return df


def create_amount(df: pd.DataFrame) -> pd.DataFrame:
    df["Amount"] = df["Quantity"] * df["Price"]

    return df


def modify_country(df: pd.DataFrame) -> pd.DataFrame:
    country = df.groupby("Customer_ID")["Country"].agg(lambda x: x.mode().iloc[0])

    df["Country"] = df["Customer_ID"].map(country)

    return df


def create_week_day(df: pd.DataFrame) -> pd.DataFrame:
    df["Week_Day"] = df["InvoiceDate"].dt.day_name()

    return df


def create_hour(df: pd.DataFrame) -> pd.DataFrame:
    df["Hour"] = df["InvoiceDate"].dt.hour

    return df


def create_month(df: pd.DataFrame) -> pd.DataFrame:
    df["Month"] = df["InvoiceDate"].dt.month

    return df


def create_date(df: pd.DataFrame) -> pd.DataFrame:
    df["Date"] = df["InvoiceDate"].dt.date

    return df
