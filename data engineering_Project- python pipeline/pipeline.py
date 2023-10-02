import pyodbc
import mysql.connector

# Connect to SQL Server (AdventureWorksDW2022 database)
server_name = 'AtlasLaptop'
database_name = 'AdventureWorksDW2022'

# Construct the connection string for the default instance (Null)
sql_server_conn = pyodbc.connect(f'Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection=yes;')
cursor_sql_server = sql_server_conn.cursor()

# Connect to MySQL (myfirstetl database in XAMPP)
mysql_conn = mysql.connector.connect(host='localhost', user='root', password='', database='myfirstetl')
cursor_mysql = mysql_conn.cursor()

# Rest of your ETL code...

# Step 1: Extract Data from SQL Server (AdventureWorksDW2022)
cursor_sql_server.execute('SELECT FirstName, LastName, EmailAddress, Phone FROM dbo.DimCustomer')
data_to_load = cursor_sql_server.fetchall()

# Step 2: Transform Data (if needed)
# In this example, we're not performing significant transformation, just mapping columns.

# Step 3: Load Data into MySQL (my_table)
for row in data_to_load:
    cursor_mysql.execute('''
        INSERT INTO my_table (FirstName, LastName, Email, Phone)
        VALUES (%s, %s, %s, %s)
    ''', (
        row.FirstName,
        row.LastName,
        row.EmailAddress,
        row.Phone
    ))
    mysql_conn.commit()

# Close connections
cursor_sql_server.close()
sql_server_conn.close()
cursor_mysql.close()
mysql_conn.close()


