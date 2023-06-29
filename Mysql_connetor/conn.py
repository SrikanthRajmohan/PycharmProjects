# import mysql.connector
#
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Srikanth29@",
#     database="bhavcopy"
# )
#
# # Create a cursor object to interact with the database
# cursor = conn.cursor()
#
# # Execute a SELECT query
# query = "SELECT * FROM newschema;"
# cursor.execute(query)
#
# # Fetch all the rows returned by the query
# rows = cursor.fetchall()
#
# # Iterate over the rows and print the data
# for data in rows:
#     print(data)
#
# # Close the cursor and connection
# cursor.close()
# conn.close()
# #
# import mysql.connector
#
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Srikanth29@",
#     database="newschema"
#
# )
#
# # Create a cursor object to interact with the database
# cursor = conn.cursor()
#
# # Execute a SELECT query
# query = "SELECT * FROM newschema.bhavcopy;;"
# cursor.execute(query)
#
# # Fetch all the rows returned by the query
# rows = cursor.fetchall()
# for data in rows:
#     print(data)
#
# import mysql.connector
# from configparser import ConfigParser
#
# # Read the configuration from the file
# config = ConfigParser()
# config.read('config.ini')
#
# # Retrieve the database configuration values
# db_config = config['mysql']
#
# # Connect to the database using the configuration values
# conn = mysql.connector.connect(
#     host=db_config['host'],
#     user=db_config['user'],
#     password=db_config['password'],
#     database=db_config['database']
# )
# cursor = conn.cursor()
#
# # Rest of your code remains the same
# date = "2023-06-23"
# select_query = f"SELECT * FROM table_name WHERE date_column = '{date}'"
#
# # ...
#
# import mysql.connector
# from configparser import ConfigParser
#
# # Read the configuration file
# config = ConfigParser()
# config.read('/path/to/config.ini')
#
#
# # Retrieve connection details from the configuration file
# host = config.get('mysql', 'host')
# user = config.get('mysql', 'user')
# password = config.get('mysql', 'Srikanth29@')
# database = config.get('mysql', 'newschema')
#
# # Create a connection to the MySQL server
# conn = mysql.connector.connect(
#     host=host,
#     user=user,
#     password='Srikanth29@',
#     database='newschema'
# )
#
# # Create a cursor object to interact with the database
# cursor = conn.cursor()
#
# # Execute a SELECT query
# query = "SELECT * FROM newschema.bhavcopy"
# cursor.execute(query)
#
# # Fetch all the rows returned by the query
# rows = cursor.fetchall()
# for data in rows:
#     print(data)
#
# # Close the cursor and connection
# cursor.close()
# conn.close()

import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Srikanth29@",
    database="newschema"
)

cursor = conn.cursor()

query = "SELECT * FROM newschema.bhavcopy"
cursor.execute(query)

rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=cursor.column_names)

print(df)

cursor.close()
conn.close()

# import mysql.connector
# from configparser import ConfigParser
#
# # Read the configuration file
# config = ConfigParser()
# config.read('config.ini')
#
#
# # Retrieve connection details from the configuration file
# host = config.get('mysql', 'host')
# user = config.get('mysql', 'user')
# password = config.get('mysql', 'Srikanth29@')
# database = config.get('mysql', 'newschema')
#
# # Create a connection to the MySQL server
# conn = mysql.connector.connect(
#     host=host,
#     user=user,
#     password='Srikanth29@',
#     database='newschema'
# )
#
# # Create a cursor object to interact with the database
# cursor = conn.cursor()
#
# # Execute a SELECT query
# query = "SELECT * FROM newschema.bhavcopy"
# cursor.execute(query)
#
# # Fetch all the rows returned by the query
# rows = cursor.fetchall()
# for data in rows:
#     print(data)

# Close the cursor and connection
# cursor.close()
# conn.close()
#
# import mysql.connector
# from configparser import ConfigParser
#
# # Read the configuration file
# config = ConfigParser()
# config.read('config.ini')
#
# # Retrieve connection details from the configuration file
# host = config.get('mysql', 'host')
# user = config.get('mysql', 'user')
# password = config.get('mysql', 'Srikanth29@')
# database = config.get('mysql', 'newschema')
#
# # Create a connection to the MySQL server
# conn = mysql.connector.connect(
#     host=host,
#     user=user,
#     password='Srikanth29@',
#     database='newschema'
# )
#
# # Create a cursor object to interact with the database
# cursor = conn.cursor()
#
# # Execute a SELECT query
# query = "SELECT * FROM newschema.bhavcopy"
# cursor.execute(query)
#
# # Fetch all the rows returned by the query
# rows = cursor.fetchall()
# for data in rows:
#     print(data)
#
# # Close the cursor and connection
# cursor.close()
# conn.close()
