import sqlite3

import pandas as pd

from . import *

excel = pd.read_excel(RAW_CSV_DIR)

connection = sqlite3.connect(INPUT_DIR)

excel.to_sql("retail", connection, index=False, if_exists="replace")
