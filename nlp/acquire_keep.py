import pandas as pd
import numpy as np
import os

# JSON API
import requests
import json

def get_items():
    #gets items from Zachs lol server for time series analysis project
    print('Checking for existing items.csv...')
    if os.path.exists('items.csv'):
        print('Reading items from local csv...\n')
        return pd.read_csv('items.csv')
    print('csv does not exist... pulling new data to create csv...')
    base_url = 'https://python.zach.lol'
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    items = pd.DataFrame(data['payload']['items'])
    response = requests.get(base_url + data['payload']['next_page'])
    data = response.json()
    while data['payload']['page'] <= data['payload']['max_page']:
        items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index(drop=True)
        if data['payload']['page'] == data['payload']['max_page']:
            break
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
    print('writing items.csv...')
    items.to_csv('items.csv', index=False)
    print('finished writing items.csv.  Part 1 done.\n')
    print('items.tail:\n')
    print(items.tail())
    print('\n')
    return items

def get_stores():
    # #gets stores from Zachs lol server for time series analysis project
    print('Checking for existing stores.csv...')
    if os.path.exists('stores.csv'):
        print('Reading stores from local csv...\n')
        return pd.read_csv('stores.csv')
    print('csv does not exist... pulling new data to create csv...')
    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    print('writing stores.csv...')
    stores.to_csv('stores.csv', index=False)
    print('finished writing stores.csv.  Part 2 done.\n')
    print('stores.tail:\n')
    print(stores.tail())
    print('\n')
    return stores

def get_sales():
    #gets sales from Zachs lol server for time series analysis project
    print('Checking for existing sales.csv...')
    if os.path.exists('sales.csv'):
        print('Reading sales from local csv...\n')
        return pd.read_csv('sales.csv')
    print('csv does not exist... pulling new data to create csv...')
    base_url = 'https://python.zach.lol'
    response = requests.get('https://python.zach.lol/api/v1/sales')
    data = response.json()
    sales = pd.DataFrame(data['payload']['sales'])
    response = requests.get(base_url + data['payload']['next_page'])
    data = response.json()
    while data['payload']['page'] <= data['payload']['max_page']:
        sales = pd.concat([sales, pd.DataFrame(data['payload']['sales'])]).reset_index(drop=True)
        if data['payload']['page'] == data['payload']['max_page']:
            break
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
    print('writing sales.csv...')
    sales.to_csv('sales.csv', index=False)
    print('finished writing sales.csv.  Part 3 done.\n')
    print('sales.tail:\n')
    print(sales.tail())
    print('\n')
    return sales

def tsa_acquire_all():
# #gets final df from my harddrive for time series analysis project
# print('Checking for existing df.csv...')
# if os.path.exists('df.csv'):
#     print('Reading sales from local csv...\n')
#     return pd.read_csv('df.csv')
    items = get_items()
    stores = get_stores()
    sales = get_sales()
    sales.rename(columns={'store': 'store_id', 'item': 'item_id'}, inplace=True)
    df = pd.merge(sales, items, on='item_id')
    df = pd.merge(df, stores, on='store_id')
    print('Writing final df.csv...\n')
    df.to_csv('df.csv', index=False)
    print('Finished writing final df.csv.  Final df done.\n')
    print('HEADS UP: finished all tsa acquire.  Full Stop!\n')
    print('Final raw df now ready to begin data preparations.\n')
    # print('Heres a look at the tail of the final df:\n')
    # print(df.tail())
    print('\n')
    return df

#tsa_acquire_all()

# The code below inspires by Michael P. Moran's missing_vals_df().
def missing_values_col(df):
	"""
	Write or use a previously written function to return the
	total missing values and the percent missing values by column.
	"""
	null_count = df.isnull().sum()
	null_percentage = (null_count / df.shape[0]) * 100
	empty_count = pd.Series(((df == ' ') | (df == '')).sum())
	empty_percentage = (empty_count / df.shape[0]) * 100
	nan_count = pd.Series(((df == 'nan') | (df == 'NaN')).sum())
	nan_percentage = (nan_count / df.shape[0]) * 100
	return pd.DataFrame({'num_missing': null_count, 'missing_percentage': null_percentage,
	                     'num_empty': empty_count, 'empty_percentage': empty_percentage,
	                     'nan_count': nan_count, 'nan_percentage': nan_percentage})


def peekatdata(df):
    print("\n \n SHAPE:")
    print(df.shape)

    print("\n \n COLS:")
    print(df.columns)

    print("\n \n INFO:")
    print(df.info())

    print("\n \n Missing Values:")
    missing_vals = df.columns[df.isnull().any()]
    print(df.isnull().sum())

    print("\n \n DESCRIBE:")
    print(df.describe())

    print('\n \n HEAD:')
    print(df.head(5))

    print('\n \n TAIL:' )
    print(df.tail(5))
