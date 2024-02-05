import pandas as pd

def convert_toNumeric(transformed_table: pd.DataFrame):
    """ Convert columns that needs to be in integer or float"""

    transformed_table = transformed_table.dropna(how='any')

    # Convert 'order_id' to integer, replace non-numeric values with NaN
    transformed_table.loc[:, 'order_id'] = pd.to_numeric(transformed_table['order_id'], errors='coerce')
    transformed_table = transformed_table.dropna(subset=['order_id'])
    transformed_table['order_id'] = transformed_table['order_id'].astype('Int64')

    # Convert 'quantity_ordered' to integer, replace non-numeric values with NaN
    transformed_table['quantity_ordered'] = pd.to_numeric(transformed_table['quantity_ordered'], errors='coerce')

    # Convert 'price_each' to float, replace non-numeric values with NaN
    transformed_table['price_each'] = pd.to_numeric(transformed_table['price_each'], errors='coerce')

    return transformed_table


def convert_toDate(transformed_table: pd.DataFrame):
    """ Convert columns that needs to be in datetime format"""

    # Convert 'order_date' to datetime
    transformed_table['order_date'] = pd.to_datetime(transformed_table['order_date'], errors='coerce')

    # Extract yy, mm, dd from the order date
    transformed_table['order_year'] = transformed_table['order_date'].dt.year
    transformed_table['order_month'] = transformed_table['order_date'].dt.strftime('%b')
    transformed_table['order_day'] = transformed_table['order_date'].dt.day

    return transformed_table


def convert_toString(transformed_table: pd.DataFrame):
    """ Convert columns that needs to be in integer or float"""

    # Ensure 'product' column is of string type
    transformed_table['product'] = transformed_table['product'].astype(str)

    # Ensure 'purchase_address' column is of string type
    transformed_table['address'] = transformed_table['address'].astype(str)

    return transformed_table


def split_address(transformed_table: pd.DataFrame):
    """ split address into multiple columns"""

    address_split = transformed_table['address'].str.split(', ', expand=True)
    transformed_table['street'] = address_split[0]
    transformed_table['city'] = address_split[1]
    transformed_table['state'] = address_split[2]

    zip_split = transformed_table['state'].str.split(' ', expand=True)
    transformed_table['state'] = zip_split[0]
    transformed_table['zip'] = zip_split[1]

    transformed_table['country'] = "United States"

    return transformed_table


def transform_sales(staging_table: pd.DataFrame):
    transformed_table = staging_table.copy()

    transformed_table = convert_toNumeric(transformed_table)
    transformed_table = convert_toDate(transformed_table)
    transformed_table = convert_toString(transformed_table)
    transformed_table = split_address(transformed_table)

    # Rearrange columns
    transformed_table = transformed_table[['order_id',
                                           'order_year',
                                           'order_month',
                                           'order_day',
                                           'product',
                                           'quantity_ordered',
                                           'price_each',
                                           'street',
                                           'city',
                                           'state',
                                           'zip',
                                           'country']]
    # drop null values
    transformed_table = transformed_table.dropna(how='any')
    # Remove duplicates
    transformed_table.drop_duplicates(subset=['order_id'], inplace=True)

    return transformed_table