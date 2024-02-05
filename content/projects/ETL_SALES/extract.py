# Import libraries needed
import psycopg2
import glob
import pandas as pd


# function extracting from excel
def consolidated_sales_excel():
    # excel file path
    excel_file_path = r'C:\Users\\Public\Sales_January_April_2019.xlsx'

    sales_excel = pd.read_excel(excel_file_path, sheet_name=None)

    excel_df = pd.concat(sales_excel.values(), ignore_index=True)

    return excel_df


# function extracting from csv
def consolidated_sales_csv():
    new_folder = r'C:\Users\Public\sales_csv'
    csv_files = glob.glob(f'{new_folder}/*.csv')

    if csv_files:
        csv_df = []

        for csv_file in csv_files:
            csv_df.append(pd.read_csv(csv_file))

            csv_dfs = pd.concat(csv_df, ignore_index=True)

        return csv_dfs
    else:
        print("There is no file in folder.")


# function extracting from database
def consolidated_sales_db():
    # PostgreSQL connection parameters
    pg_username = 'dummy'
    pg_password = 'dummy'
    pg_host = 'dummy'
    pg_port = 'dummy'
    pg_database = 'sales_sep_dec_2019'

    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        user=pg_username,
        password=pg_password,
        host=pg_host,
        port=pg_port,
        database=pg_database
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # SQL query to extract data from PostgreSQL table
    sql_query = 'SELECT * FROM sales_db'

    # Execute the query
    cursor.execute(sql_query)

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Get the column names from the cursor description
    column_names = [desc[0] for desc in cursor.description]

    # Create a pandas DataFrame using the fetched data and column names
    pg_df = pd.DataFrame(rows, columns=column_names)

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return pg_df


def consolidated_data():
    result_excel = consolidated_sales_excel()
    result_csv = consolidated_sales_csv()
    result_db = consolidated_sales_db()

    # Concatenate the DataFrames vertically
    consolidated_result = pd.concat([result_excel, result_csv], ignore_index=True)

    # renaming columns
    consolidated_result = consolidated_result.rename(columns={'Order ID': 'order_id',
                                                              'Product': 'product',
                                                              'Quantity Ordered': 'quantity_ordered',
                                                              'Price Each': 'price_each',
                                                              'Order Date': 'order_date',
                                                              'Purchase Address': 'address'})
    consolidated_result = pd.concat([consolidated_result, result_db], ignore_index=True)

    return consolidated_result
