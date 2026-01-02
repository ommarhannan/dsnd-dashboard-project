import sqlite3
from query_base import QueryBase
from sql_execution import QueryMixin

'''
#testing the query base file
testobject = QueryBase(table_name="employee")
print(testobject.names())
print(testobject.event_counts(id=4))
print(testobject.notes(id=4))
'''

#testing the employee.py file


'''
testobject2 = QueryMixin()

sql_string = "SELECT first_name, last_name FROM employee"
print(testobject2.pandas_query(sql_string))
'''



