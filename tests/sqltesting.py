# Import any dependencies needed to execute sql queries

import sqlite3
from pathlib import Path
from sql_execution import db_path
import pandas as pd


def pandas_query(sql_string):

    # set up connection to database

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    df = pd.read_sql_query(sql_string, connection)
    connection.close()
    return df

test_string = "SELECT * FROM employee_events"

new_df = pandas_query(test_string)

print(new_df)

