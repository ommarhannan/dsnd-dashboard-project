import sqlite3
import pandas as pd
from pathlib import Path
from sql_execution import db_path
from employee import Employee

newobject = Employee()

print(newobject.username(id=4))

