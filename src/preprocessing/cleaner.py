import pandas as pd


# ==========================================================================
# -- standardize column names and values in columns with string data type --
# ==========================================================================
def standardize(
    df: pd.DataFrame,
    columns: list[str] | None = None,
    standardize_columns: bool = False,
) -> pd.DataFrame:
    if standardize_columns:
        df.columns = df.columns.str.strip().str.replace(" ", "_")

    if columns is not None:
        for column in columns:
            df[column] = (
                # Remove leading and trailing spaces, convert to uppercase,
                # and replace consecutive spaces with a single space.
                df[column]
                .str.strip()
                .str.upper()
                .str.replace(r"\s+", " ", regex=True)
            )

    return df


# =========================================================================
# -------------- remove rows with missing customer IDs --------------------
# =========================================================================
def clean_customer_id(df: pd.DataFrame) -> pd.DataFrame:
    df.dropna(subset=["Customer_ID"], inplace=True)

    return df


# =========================================================================
# -------------- remove invoices that start with 'C' --------------------
# =========================================================================
def clean_invoice(df: pd.DataFrame) -> pd.DataFrame:
    df = df[~df["Invoice"].str.startswith("C", na=False)]

    return df


# =========================================================================
# ------ remove non-product stock codes and test/adjustment entries ------
# =========================================================================
def clean_stock_code(df: pd.DataFrame) -> pd.DataFrame:
    codes_to_remove = [
        "BANK CHARGES",
        "POST",
        "D",
        "M",
        "C2",
        "PADS",
        "ADJUST",
        "TEST001",
        "TEST002",
        "ADJUST2",
        "SP1002",
    ]

    df = df[~df["StockCode"].isin(codes_to_remove)]

    return df


# =========================================================================
# --------------- remove rows with zero or negative prices ---------------
# =========================================================================
def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["Price"] > 0]

    return df


# =========================================================================
# ------------ convert invoice dates to datetime data type ------------
# =========================================================================
def clean_invoice_date(df: pd.DataFrame) -> pd.DataFrame:
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    return df


# ========================================================================
# --- apply all cleaning functions in the required preprocessing order ---
# ========================================================================
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Standardize column names and string values.
    df = standardize(df)

    # Remove rows with missing customer IDs.
    df = clean_customer_id(df)

    # Remove canceled invoices.
    df = clean_invoice(df)

    # Remove non-product and invalid stock codes.
    df = clean_stock_code(df)

    # Remove rows with zero or negative prices.
    df = clean_prices(df)

    # Convert invoice dates to datetime.
    df = clean_invoice_date(df)

    return df
