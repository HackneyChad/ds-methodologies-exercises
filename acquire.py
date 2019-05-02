# import titanic and iris data
# 28Mar19

import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

iris_query = '''
SELECT m.species_id
    ,s.species_name
    ,measurement_id
    ,petal_length
    ,petal_width
    ,sepal_length
    ,sepal_width
FROM measurements m
JOIN species s ON s.species_id = m.species_id
    ORDER by m.species_id, m.measurement_id;
'''

# def get_iris_data():
#     return pd.read_sql('SELECT * FROM species JOIN measurements USING (species_id)', get_connection('iris_db'))

def get_iris_data():
    return pd.read_sql(iris_query, get_connection('iris_db'))



def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.read_sql('select * from passengers', get_connection('titanic_db'))

#=======#

# def get_connection(db, user=env.username, host=env.hostname, password=env.password):
#     return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# def get_titanic_data():
#     return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

