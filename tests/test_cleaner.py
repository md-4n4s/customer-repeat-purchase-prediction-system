from src.preprocessing.cleaning.cleaner import *

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
