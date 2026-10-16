import pandas as pd

DROP = [
    "Customer_ID",
    "Date",
    "Mean_Quantity",
    "Max_Quantity",
    "Min_Quantity",
    "Mean_Price",
    "Median_Price",
    "Std_Price",
    "Mean_Description_Length",
    "Mean_Amount_Per_Product",
    "Mean_Unique_Products_Per_Invoice",
    "Median_Unique_Products_Per_Invoice",
    "Median_Quantity_Per_Invoice",
    "Median_Amount_Per_Invoice",
    "Std_Amount_Per_Invoice",
    "Mode_Hour",
    "Customer_Span_Days",
    "Mean_Days_Between_Purchases",
    "Max_Days_Between_Purchases",
    "Min_Days_Between_Purchases",
    "Std_Days_Between_Purchases"
]

# Engineer and test
ENGINEER = ["Range_Quantity"]

TEST = [
    "Top_Product_Ratio",
    "Mean_Products_Per_Invoice",
    "Mean_Quantity_Per_Invoice",
    "Mean_Amount_Per_Invoice",
    "Mode_Week_Day"
]

# Test with and without each other
TEST_CONDITIONAL = [
    "Total_Invoice",
    "Unique_Purchase_Dates"
]

KEEP = [
    "Country",
    "Total_Quantity",
    "Total_Amount",
    "Unique_Products",
    "Has_Multi_Description_Length",
    "Is_First_Purchase",
    "Repeat_Product_Ratio",
    "Max_Quantity_Per_Invoice",
    "Max_Amount_Per_Invoice",
    "Days_Since_Last_Purchase",
    "Unique_Purchase_Week_Days",
]

def drop_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df = df.drop(columns=columns)

    return df

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    df["Range_Quantity"] = df["Max_Quantity"] - df["Min_Quantity"]

    df = drop_columns(df, DROP)


    return df
