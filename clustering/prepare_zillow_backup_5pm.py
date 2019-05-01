import acquire_zillow as acq
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def get_full_zillow():
    '''pulls in the entire 2016-2017 zillow master set'''
    df = pd.read_csv('zillow.csv')
    return df

def singles_only(df):
    '''looks at single units only'''
    singles = ['Single Family Residential']
    # singles = ['Cluster Home', 'Condominium', 'Cooperative', 'Manufactured, Modular, Prefabricated Homes', 'Mobile Home', 'Residential General', 'Single Family Residential', 'Townhouse']
    df = df[df.propertylandusedesc.isin(singles)] 
    return df

def nums_to_obj(df):
    df[['parcelid', 'fips', 'regionidcity', 'regionidcounty', 'regionidzip', 'yearbuilt', 'censustractandblock']] = df[['parcelid', 'fips', 'regionidcity', 'regionidcounty', 'regionidzip', 'yearbuilt', 'censustractandblock']].astype(str)
    return df

def remove_columns(df, cols_to_remove):  
    df = df.drop(columns=cols_to_remove)
    return df

def handle_missing_values(df, prop_required_column = .75, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

# def fill_unitcnt(df):
#     df['unitcnt'] = df['unitcnt'].fillna(value=0, inplace = True)
#     return df

# def fill_all_others(df):
#     df = df.calcfillna(0, inplace = True)
#     return df


def drop_nans_yearbuilt(df):
    df = df[df.yearbuilt != 'nan']
    return df

def drop_nans_regionidcity(df):
    df = df[df.regionidcity != 'nan']
    return df

def drop_nans_regionidzip(df):
    df = df[df.regionidzip != 'nan']
    return df

def drop_nans_censustractandblock(df):
    df = df[df.censustractandblock != 'nan']
    return df 

# def fill_taxamount(df):
#     df = df.taxamount.fillna(0)
#     return df

# def fill_taxvaluedollarcnt(df):
#     df = df.taxvaluedollarcnt.fillna(0)
#     return df

# def fill_calculatedfinishedsquarefeet(df):
#     df = df.calculatedfinishedsquarefeet.fillna(0)
#     return df

def check_missing_values_col(df):
	'''
	Write or use a previously written function to return the
	total missing values and the percent missing values by column.
	'''
	null_count = df.isnull().sum()
	null_percentage = (null_count / df.shape[0]) * 100
	empty_count = pd.Series(((df == ' ') | (df == '')).sum())
	empty_percentage = (empty_count / df.shape[0]) * 100
	nan_count = pd.Series(((df == 'nan') | (df == 'NaN')).sum())
	nan_percentage = (nan_count / df.shape[0]) * 100
	return pd.DataFrame({'num_missing': null_count, 'missing_percentage': null_percentage,
	                     'num_empty': empty_count, 'empty_percentage': empty_percentage,
	                     'nan_count': nan_count, 'nan_percentage': nan_percentage})

def field_drop(df):
    df = df.drop(columns=(['calculatedbathnbr',
    'finishedsquarefeet12','assessmentyear','roomcnt',
    'landtaxvaluedollarcnt','structuretaxvaluedollarcnt','rawcensustractandblock',
    'lotsizesquarefeet','fullbathcnt']))
    return df

def drop_remaining_missing(df):
    df = df.dropna()
    return df

#Erics logic for trimming outliers: Removing outliers beyond three standard deviations from all columns:
#df_fixed = df_join[(np.abs(stats.zscore(df_join)) < 3).all(axis=1)]

def data_prep(df, cols_to_remove=[], prop_required_column=.75, prop_required_row=.75):
    df = nums_to_obj(df)
    df = singles_only(df)
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)
    # df = fill_unitcnt(df)
    # df = fill_all_others(df)
    # df = drop_remaining_missing(df)
    df = drop_nans_yearbuilt(df)
    df = drop_nans_regionidcity(df)
    df = drop_nans_regionidzip(df)
    df = drop_nans_censustractandblock(df)
    df = field_drop(df)
    # df = fill_taxamount(df)
    # df = fill_taxvaluedollarcnt(df)
    # df = fill_calculatedfinishedsquarefeet(df)
    df = drop_remaining_missing(df)
    return df


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
