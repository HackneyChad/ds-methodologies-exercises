import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import acquire

# prep iris data
df_i = acquire.get_iris_data()

def drop_columns(df):
        df = df.drop(columns=['measurement_id', 'species_id'], axis=1)
        return df

def rename_columns(df):
        df.rename(columns={'species_name': 'species'}, inplace=True)
        return df

def encode_species(df):
        encoder = LabelEncoder()
        encoder.fit(df.species)
        df.species = encoder.transform(df.species)
        return df

def prep_iris(df):
        df = drop_columns(df)
        df = rename_columns(df)
        df = encode_species(df)
        return df

df_i = prep_iris(df_i)


# prep titanic data
df_t = acquire.get_titanic_data()

def handle_missing_values(df):
        df.embark_town.fillna('Other', inplace=True)
        df.embarked.fillna('O', inplace=True)
        df.age.fillna(df.age.median(), inplace=True)
        return df

def drop_columns(df):
        df = df.drop(columns=['deck'], axis=1)
        return df

def encode_embarked(df):
        encoder = LabelEncoder()
        encoder.fit(df.embarked)
        embarked = encoder.transform(df.embarked)
        return df
    
def prep_titanic(df):
        df = handle_missing_values(df)
        df = drop_columns(df)
        df = encode_embarked(df)
        return df
  
df_t = prep_titanic(df_t)
