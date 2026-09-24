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
