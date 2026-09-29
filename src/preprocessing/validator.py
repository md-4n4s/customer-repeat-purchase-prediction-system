from collections.abc import Callable
from functools import wraps

import pandas as pd

from .exceptions import *


def check_missing_values(func: Callable) -> Callable:
    """Check that the specified column contains no missing values."""

    @wraps(func)
    def wrapper(df: pd.DataFrame, column: str, *args, **kwargs) -> None:
        if df[column].isnull().any():
            raise InvalidFieldException(f"{column} contains missing values.")

        return func(df, column, *args, **kwargs)

    return wrapper


def check_data_type(func: Callable) -> Callable:
    """Check that the specified column has the expected data type."""

    @wraps(func)
    def wrapper(df: pd.DataFrame, column: str, dtype: str) -> None:
        if df[column].dtype != dtype:
            raise InvalidFieldTypeException(f"{column} should be of type {dtype}.")

        return func(df, column, dtype)

    return wrapper


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


@check_data_type
@check_missing_values
def validate_basic(df: pd.DataFrame, column: str, dtype: str) -> None:
    """Validate a column for missing values, and data type."""


def validate_invoice(df: pd.DataFrame, column: str, dtype: str) -> None:
    """Validate the Invoice column for missing values, data type, and format."""

    validate_basic(df, column, dtype)

    if not df["Invoice"].str.isdigit().all():
        raise InvalidFieldException("Invoice should contain only digits.")


def validate_stock_code(df: pd.DataFrame, column: str, dtype: str) -> None:
    """Validate the StockCode column for missing values, data type, and format."""

    validate_basic(df, column, dtype)

    if df["StockCode"].str.match(r"^\D").any():
        raise InvalidFieldException(
            "StockCode contains values that start with a non-digit."
        )


def validate_positive(df: pd.DataFrame, column: str, dtype: str) -> None:
    """Validate a column for missing values, data type, and positive values."""

    validate_basic(df, column, dtype)

    check_negative_or_zero_values(df, column)


@check_missing_values
def validate_invoice_date(
    df: pd.DataFrame, column: str, dtype: str | None = None
) -> None:
    """Validate the InvoiceDate column for missing values and datetime type."""

    if not pd.api.types.is_datetime64_any_dtype(df["InvoiceDate"]):
        raise InvalidFieldTypeException("InvoiceDate must be a datetime column.")


def validate(df: pd.DataFrame) -> None:
    """Validate all required fields and dataset-level requirements."""
    validate_dataset(df)
    validate_basic(df, "Customer_ID", "float64")
    validate_invoice(df, "Invoice", "str")
    validate_stock_code(df, "StockCode", "str")
    validate_basic(df, "Description", "str")
    validate_positive(df, "Quantity", "int64")
    validate_positive(df, "Price", "float64")
    validate_basic(df, "Country", "str")
    validate_invoice_date(df, "InvoiceDate")
