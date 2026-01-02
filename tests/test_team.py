import sqlite3
import pandas as pd
from pathlib import Path
from sql_execution import db_path
from team import Team

newobject = Team()

print(newobject.names())