import sqlite3
from pathlib import Path

import pandas as pd


# ============================================================
# --  create database connection and load data from retail  --
# ============================================================
def load_data(path: Path):
    connection = sqlite3.connect(path)

    df = pd.read_sql("SELECT * FROM retail", connection)

    connection.close()

    return df


# ============================================================
# -------------  store data in required format  -------------
# ============================================================
def save_data(df: pd.DataFrame, path: Path) -> None:
    if path.suffix == ".csv":
        df.to_csv(path, index=False)

    else:
        connection = sqlite3.connect(path)

        df.to_sql("retail", connection, index=False, if_exists="replace")

        connection.close()
