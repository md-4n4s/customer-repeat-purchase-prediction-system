from src.preprocessing.cleaning.cleaner import *
import numpy as np

def test_standardize() -> None:
    original = pd.DataFrame({
        " Customer Id    ": ["1", "2", "3", "4"],
        " Customer Name  ": ["ali", "  john", "muhammad      anas     ", "SARA"],
        "City": ["Lahore", "Karachi", "London", "New York"]
    })

    result = standardize(original, columns=[" Customer Name  "], standardize_columns=True)

    expected = pd.DataFrame({
        "Customer_Id": ["1", "2", "3", "4"],
        "Customer_Name": ["ALI", "JOHN", "MUHAMMAD ANAS", "SARA"],
        "City": ["Lahore", "Karachi", "London", "New York"]
    })

    pd.testing.assert_frame_equal(result, expected)

def test_clean_duplicates() -> None:
    original = pd.DataFrame({
        "Customer_Id": ["1", "2", "1", "4"],
        "Customer_Name": ["ALI", "JOHN", "ALI", "JOHN"],
        "City": ["Karachi", "Karachi", "Karachi", "New York"]
    })

    result = clean_duplicates(original)

    expected = pd.DataFrame({
        "Customer_Id": ["1", "2", "4"],
        "Customer_Name": ["ALI", "JOHN", "JOHN"],
        "City": ["Karachi", "Karachi", "New York"]
    })

    pd.testing.assert_frame_equal(result, expected)

def test_clean_customer_id() -> None:
    original = pd.DataFrame({
        "Customer_ID": ["1", "2", "1", np.nan],
        "Customer_Name": ["ALI", "JOHN", "ALI", "JOHN"]
    })

    result = clean_customer_id(original)

    expected = pd.DataFrame({
        "Customer_ID": ["1", "2", "1"],
        "Customer_Name": ["ALI", "JOHN", "ALI"]
    })

    pd.testing.assert_frame_equal(result, expected)

def test_clean_invoice() -> None:
    original = pd.DataFrame({
        "Customer_Id": ["1", "2", "4"],
        "Invoice": ["212", "C13", np.nan]
    })

    result = clean_invoice(original)

    expected = pd.DataFrame({
        "Customer_Id": ["1", "4"],
        "Invoice": ["212", np.nan]
    })

    pd.testing.assert_frame_equal(result, expected)
