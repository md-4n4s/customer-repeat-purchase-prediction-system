import numpy as np

from src.preprocessing.cleaning.cleaner import *


def test_standardize() -> None:
    original = pd.DataFrame(
        {
            " Customer Id    ": ["1", "2", "3", "4"],
            " Customer Name  ": ["ali", "  john", "muhammad      anas     ", "SARA"],
            "City": ["Lahore", "Karachi", "London", "New York"],
        }
    )

    result = standardize(
        original, columns=[" Customer Name  "], standardize_columns=True
    )

    expected = pd.DataFrame(
        {
            "Customer_Id": ["1", "2", "3", "4"],
            "Customer_Name": ["ALI", "JOHN", "MUHAMMAD ANAS", "SARA"],
            "City": ["Lahore", "Karachi", "London", "New York"],
        }
    )

    pd.testing.assert_frame_equal(result, expected)


def test_clean_duplicates() -> None:
    original = pd.DataFrame(
        {
            "Customer_Id": ["1", "2", "1", "4"],
            "Customer_Name": ["ALI", "JOHN", "ALI", "JOHN"],
            "City": ["Karachi", "Karachi", "Karachi", "New York"],
        }
    )

    result = clean_duplicates(original)

    expected = pd.DataFrame(
        {
            "Customer_Id": ["1", "2", "4"],
            "Customer_Name": ["ALI", "JOHN", "JOHN"],
            "City": ["Karachi", "Karachi", "New York"],
        }
    )

    pd.testing.assert_frame_equal(result, expected)


def test_clean_customer_id() -> None:
    original = pd.DataFrame(
        {
            "Customer_ID": ["1", "2", "1", np.nan],
            "Customer_Name": ["ALI", "JOHN", "ALI", "JOHN"],
        }
    )

    result = clean_customer_id(original)

    expected = pd.DataFrame(
        {"Customer_ID": ["1", "2", "1"], "Customer_Name": ["ALI", "JOHN", "ALI"]}
    )

    pd.testing.assert_frame_equal(result, expected)


def test_clean_invoice() -> None:
    original = pd.DataFrame(
        {"Customer_Id": ["1", "2", "4"], "Invoice": ["212", "C13", np.nan]}
    )

    result = clean_invoice(original)

    expected = pd.DataFrame({"Customer_Id": ["1", "4"], "Invoice": ["212", np.nan]})

    pd.testing.assert_frame_equal(result, expected)


def test_clean_stock_code() -> None:
    original = pd.DataFrame(
        {
            "StockCode": [
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
                "ALLOWED",
                "3938",
            ]
        }
    )

    result = clean_stock_code(original)

    expected = pd.DataFrame({"StockCode": ["ALLOWED", "3938"]})

    pd.testing.assert_frame_equal(result, expected)


def test_clean_prices() -> None:
    original = pd.DataFrame({"Price": [-2, 0, 23, 0, -4, 111]})

    result = clean_prices(original)

    expected = pd.DataFrame({"Price": [23, 111]})

    pd.testing.assert_frame_equal(result, expected)


def test_clean_invoice_date() -> None:
    original = pd.DataFrame({"InvoiceDate": ["2006-07-19"]})

    result = clean_invoice_date(original)

    expected = pd.DataFrame({"InvoiceDate": pd.to_datetime(["2006-07-19"])})

    pd.testing.assert_frame_equal(result, expected)
