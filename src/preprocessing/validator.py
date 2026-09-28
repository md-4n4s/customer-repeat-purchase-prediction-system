import pandas as pd

from .exceptions import *


def check_missing_values(df: pd.DataFrame, column: str) -> None:
    """Check that the specified column contains no missing values."""
    if df[column].isnull().any():
        raise InvalidFieldException(f"{column} contains null values.")


def check_data_type(df: pd.DataFrame, column: str, dtype: str) -> None:
    """Check that the specified column has the expected data type."""
    if df[column].dtype != dtype:
        raise InvalidFieldTypeException(f"{column} should be of type {dtype}.")


def check_negative_or_zero_values(df: pd.DataFrame, column: str) -> None:
    """Check that the specified column contains only positive values."""
    if df[column].min() <= 0:
        raise InvalidFieldException(f"{column} contains negative or zero values.")


def validate_dataset(df: pd.DataFrame) -> None:
    """Validate that all required columns are present in the dataset."""
    required_columns = [
        "Invoice",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "Price",
        "Customer_ID",
        "Country",
    ]

    # Check that all required columns are present.
    for column in required_columns:
        if column not in df.columns:
            raise MissingRequiredFieldException(f"Required field {column} is missing.")


def validate_customer_id(df: pd.DataFrame) -> None:
    """Validate the Customer_ID column for missing values and data type."""
    check_missing_values(df, "Customer_ID")

    check_data_type(df, "Customer_ID", "float64")


def validate_invoice(df: pd.DataFrame) -> None:
    """Validate the Invoice column for missing values, data type, and format."""
    check_missing_values(df, "Invoice")

    check_data_type(df, "Invoice", "str")

    if not df["Invoice"].str.isdigit().all():
        raise InvalidFieldException("Invoice should contain only digits.")


def validate_stock_code(df: pd.DataFrame) -> None:
    """Validate the StockCode column for missing values, data type, and format."""
    check_missing_values(df, "StockCode")

    check_data_type(df, "StockCode", "str")

    if df["StockCode"].str.match(r"^\D").any():
        raise InvalidFieldException(
            "StockCode contains values that start with a non-digit."
        )


def validate_description(df: pd.DataFrame) -> None:
    """Validate the Description column for missing values and data type."""
    check_missing_values(df, "Description")

    check_data_type(df, "Description", "str")


def validate_quantity(df: pd.DataFrame) -> None:
    """Validate the Quantity column for missing values, data type, and valid values."""
    check_missing_values(df, "Quantity")

    check_data_type(df, "Quantity", "int64")

    check_negative_or_zero_values(df, "Quantity")


def validate_price(df: pd.DataFrame) -> None:
    """Validate the Price column for missing values, data type, and valid values."""
    check_missing_values(df, "Price")

    check_data_type(df, "Price", "float64")

    check_negative_or_zero_values(df, "Price")


def validate_country(df: pd.DataFrame) -> None:
    """Validate the Country column for missing values and data type."""
    check_missing_values(df, "Country")

    check_data_type(df, "Country", "str")


def validate_invoice_date(df: pd.DataFrame) -> None:
    """Validate the InvoiceDate column for missing values and datetime type."""
    check_missing_values(df, "InvoiceDate")

    if not pd.api.types.is_datetime64_any_dtype(df["InvoiceDate"]):
        raise InvalidFieldTypeException("InvoiceDate must be a datetime column.")


def validate(df: pd.DataFrame) -> None:
    """Validate all required fields and dataset-level requirements."""
    validate_dataset(df)
    validate_customer_id(df)
    validate_invoice(df)
    validate_stock_code(df)
    validate_description(df)
    validate_quantity(df)
    validate_price(df)
    validate_invoice_date(df)
    validate_country(df)
