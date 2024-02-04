from sqlalchemy import create_engine, exc
import pandas as pd

pg_username = 'dummy'
pg_password = 'dummy'
pg_host = 'dummy'
pg_port = 'dummy'
pg_database = 'sales_sep_dec_2019'


def get_engine():
    pg_connection_string = f'postgresql://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_database}'
    engine = create_engine(pg_connection_string)
    return engine


def load_to_db(transformed_table: pd.DataFrame, table_name: str):
    engine = get_engine()

    try:
        transformed_table.to_sql(table_name, con=engine, if_exists="append", index=False)
        print(f'sales data successfully loaded into {table_name} table.')
    except exc.SQLAlchemyError as e:
        print(f'Error loading data into {table_name} table: {e}')
