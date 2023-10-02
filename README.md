# DataEngineering-ETL_Project

Project Summary: ETL Pipeline from SQL Server to MySQL

Objective: The project aims to create an Extract, Transform, Load (ETL) pipeline to transfer data from a SQL Server database (AdventureWorksDW2022) to a MySQL database (myfirstetl) using Python.

Code Overview:

SQL Server Connection:

The code establishes a connection to the SQL Server database.
The pyodbc library is used to create the connection.
The machine name "AtlasLaptop" and Windows authentication (Trusted_Connection) are used for connection details.
The target database is "AdventureWorksDW2022."
MySQL Connection:

A connection is established to the MySQL database in XAMPP.
The mysql.connector library is used for MySQL connection.
The host is set to "localhost," and Windows authentication is used (no password) with the user "root."
The target database is "myfirstetl."
Data Extraction from SQL Server:

Data is extracted from the "dbo.DimCustomer" table in the SQL Server database.
A SQL query retrieves columns such as FirstName, LastName, EmailAddress, and Phone.
The extracted data is stored in the data_to_load variable.
Data Transformation (if needed):

This code provides a placeholder for data transformation.
Depending on your specific project requirements, you can implement custom transformations in this section.
Data Loading into MySQL:

Data from data_to_load is loaded into the "my_table" table in the MySQL database.
A loop iterates through the extracted data and inserts it into the MySQL table.
The mysql_conn.commit() method is used to commit changes.
Closing Connections:

After the ETL process is completed, connections to both SQL Server and MySQL are closed.
How the Code Works:

The code establishes connections to both SQL Server and MySQL databases.

Data is extracted from SQL Server using a SQL query.

Optionally, data can be transformed as per project requirements.

Extracted and potentially transformed data is loaded into the MySQL database.

Connections to both databases are closed to ensure proper resource management.

Project Benefits:

The ETL pipeline automates the data transfer process, reducing manual effort.
It enables the transformation of data from one database system (SQL Server) to another (MySQL).
The code is adaptable and can be extended to handle more complex ETL tasks and larger datasets.
Project Conclusion:

The ETL pipeline successfully transfers data from SQL Server to MySQL, providing a foundation for data integration and analysis in a different database system. This project demonstrates the flexibility of Python for data engineering tasks and the importance of well-structured ETL processes in modern data management.
