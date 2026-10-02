import pandas as pd


def create_date_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = create_mode_feature(df, "Week_Day")

    df = create_mode_feature(df, "Hour")

    df = create_customer_span_days(df)

    df = create_days_since_last_purchase(df)

    df = create_unique_purchase_days(df)

    df = create_unique_purchase_dates(df)

    df = create_agg_days_between_purchases(df, "mean")

    df = create_agg_days_between_purchases(df, "median")

    df = create_agg_days_between_purchases(df, "max")

    df = create_agg_days_between_purchases(df, "min")

    df = create_agg_days_between_purchases(df, "std")

    return df


def create_mode_feature(df: pd.DataFrame, feature: str) -> pd.DataFrame:
    mode_feature = df.groupby("Customer_ID")[feature].agg(lambda x: x.mode().iloc[0])

    df[f"Mode_{feature.title()}"] = df["Customer_ID"].map(mode_feature)

    return df


def create_customer_span_days(df: pd.DataFrame) -> pd.DataFrame:
    age_days = df.groupby("Customer_ID")["InvoiceDate"].agg(
        lambda x: (x.max() - x.min()).days
    )

    df["Customer_Span_Days"] = df["Customer_ID"].map(age_days)

    return df


def create_days_since_last_purchase(df: pd.DataFrame) -> pd.DataFrame:
    recent = df["InvoiceDate"].max()

    last_purchases = df.groupby("Customer_ID")["InvoiceDate"].max()

    days = (recent - last_purchases).dt.days

    df["Days_Since_Last_Purchase"] = df["Customer_ID"].map(days)

    return df


def create_unique_purchase_days(df: pd.DataFrame) -> pd.DataFrame:
    unique_days = df.groupby("Customer_ID")["Week_Day"].nunique()

    df["Unique_Purchase_Week_Days"] = df["Customer_ID"].map(unique_days)

    return df


def create_unique_purchase_dates(df: pd.DataFrame) -> pd.DataFrame:
    unique_dates = df.groupby("Customer_ID")["Date"].nunique()

    df["Unique_Purchase_Dates"] = df["Customer_ID"].map(unique_dates)

    return df


def create_agg_days_between_purchases(df: pd.DataFrame, agg: str) -> pd.DataFrame:
    purchase_dates = (
        df[["Customer_ID", "Invoice", "InvoiceDate"]]
        .drop_duplicates()
        .sort_values(["Customer_ID", "InvoiceDate"])
    )

    days_between_purchases = (
        purchase_dates.groupby("Customer_ID")["InvoiceDate"]
        .diff()
        .dt.days.groupby(purchase_dates["Customer_ID"])
        .agg(agg.lower())
    )

    df[f"{agg.title()}_Days_Between_Purchases"] = df["Customer_ID"].map(
        days_between_purchases
    )

    return df
