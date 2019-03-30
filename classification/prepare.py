'''
misc functions for working with the titanic and iris dbase
'''
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def drop_i_columns(df):
    '''drops iris columns'''
    return df.drop(columns = (['measurement_id', 'species_id']))

def rename_species(df):
    '''renames species_name to species'''
    return df.rename(index = str, columns={'species_name': 'species'})

def encode_species(df):
    '''encodes species'''
    encoder = LabelEncoder()
    encoder.fit(df.species)
    return df.assign(species_encode = encoder.transform(df.species))

def prep_iris_data(df):
    '''preps all of iris data'''
    return df.pipe(drop_i_columns)\
        .pipe(rename_species)\
        .pipe(encode_species)

def handle_missing_values(df):
    '''sets missing values in embarked and embark_town'''
    return df.assign(
        embark_town = df.embark_town.fillna('Other'),
        embarked = df.embarked.fillna('O')
    )

def drop_t_columns(df):
    '''drop deck'''
    return df.drop(columns = 'deck')

def encode_embarked(df):
    '''encodes embarked'''
    encoder=LabelEncoder()
    encoder.fit(df.embarked)
    return df.assign(embarked_encode = encoder.transform(df.embarked))

def prep_titanic(df):
    '''preps all of titanic'''
    return df.pipe(handle_missing_values)\
        .pipe(drop_t_columns)\
        .pipe(encode_embarked)