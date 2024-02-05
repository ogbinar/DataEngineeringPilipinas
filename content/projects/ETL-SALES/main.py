from etl import extract,transform,load


if __name__ == "__main__":

    staging_table = extract.consolidated_data()
    transformed_table = transform.transform_sales(staging_table)
    load = load.load_to_db(transformed_table,'annual_sales_2019')

