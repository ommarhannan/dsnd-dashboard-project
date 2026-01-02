# Import any dependencies needed to execute sql queries

import sqlite3
from pathlib import Path
from sql_execution import db_path
import pandas as pd


# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE

class QueryBase:

    # create init class that takes in database name
    # and initialises a connection

    def __init__(self, table_name):

    # on initialisting object, it sets up a connection to the database
    # given as a parameter under 'db_path'
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    # Create a class attribute called `name`
    # set the attribute to an empty string
    
        self.name = table_name

    # Define a `names` method that receives
    # no passed arguments
    
    # we want to define a names method which
    # returns a list of names
    
    def names(self):
        
         # Return an empty list
        self.cursor.execute("SELECT first_name, last_name FROM employee")
        result = self.cursor.fetchall()
        #self.connection.close()
        return result

      

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE

    def event_counts(self, id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE



        sql_string = f"""
            SELECT event_date,
                SUM(positive_events) AS positive_count,
                SUM(negative_events) AS negative_count
            FROM employee_events
            WHERE {self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date
            """
        #run the query and store result in dataframe
        #for easy analysis

        df = pd.read_sql_query(sql_string, self.connection)
        return df


        

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE


    def notes(self, id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE
         
        notes_table = "notes"
        
        query = f"""
            SELECT note_date, note
            FROM {notes_table}
            WHERE {self.name}_id = {id}
            """
        df = pd.read_sql_query(query, self.connection)
        return df
        

'''
    def pandas_query(self, sql_string):

        df = pd.read_sql_query(sql_string, self.connection)
        return df

'''
