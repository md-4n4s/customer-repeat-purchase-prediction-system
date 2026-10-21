import numpy as np
import pytest

from src.preprocessing.cleaning.validator import *


def test_validate_dataset() -> None:
    with pytest.raises(MissingRequiredFieldException):
        validate_dataset(pd.DataFrame({"age": [20, 22, 21]}))


def test_validate_basic() -> None:
    with pytest.raises(InvalidFieldTypeException):
        validate_basic(pd.DataFrame({"age": [20, 22, 21]}), "age", "float64")


def test_validate_invoice() -> None:
    with pytest.raises(InvalidFieldException):
        validate_invoice(
            pd.DataFrame({"Invoice": ["20", "22D", "21"]}), "Invoice", "str"
        )


def test_validate_stock_code() -> None:
    with pytest.raises(InvalidFieldException):
        validate_stock_code(
            pd.DataFrame({"StockCode": ["A20", "D22", "21"]}), "StockCode", "str"
        )


def test_validate_positive() -> None:
    with pytest.raises(InvalidFieldException):
        validate_positive(pd.DataFrame({"age": [20, -22, 21]}), "age", "int64")


def test_check_missing_values() -> None:
    """checks_missing_values() is used in validate_basic() which is used in validate_positive()"""
    with pytest.raises(InvalidFieldException):
        validate_positive(pd.DataFrame({"dept": ["AI", np.nan, "DS"]}), "dept", "str")


def test_validate_invoice_date() -> None:
    with pytest.raises(InvalidFieldTypeException):
        validate_invoice_date(pd.DataFrame({"InvoiceDate": ["20"]}), "InvoiceDate")
