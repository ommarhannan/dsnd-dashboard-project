from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE
db_path = Path(__file__).parent/'employee_events.db'


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    
    def __init__(self):

        db_path = Path(__file__).parent/'employee_events.db'

    
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    
    def pandas_query(self, sql_string):

        # set up connection to database

        connection = connect(db_path)
        cursor = connection.cursor()
        df = pd.read_sql_query(sql_string, connection)
        connection.close()
        return df


    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    def query(sql_string):

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(sql_string)
        result = cursor.fetchall()
        connection.close()
        return result

        
    

 
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
