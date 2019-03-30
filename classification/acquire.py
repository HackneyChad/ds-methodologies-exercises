import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''initiates sql connection'''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''gets titanic data from sql dbase'''
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def get_iris_data():
    '''gets iris data from sql dbase'''
    return pd.read_sql('SELECT s.species_name, m.* FROM species s JOIN measurements m ON m.species_id = s.species_id', get_connection('iris_db'))

def get_telco_data():
    '''gets all telco data from sql dbase'''
    return pd.read_sql('\
    SELECT c.*, ct.contract_type, ist.internet_service_type, pt.payment_type FROM customers c\
    JOIN contract_types ct ON c.contract_type_id = ct.contract_type_id\
    JOIN internet_service_types ist ON c.internet_service_type_id = ist.internet_service_type_id\
    JOIN payment_types pt ON c.payment_type_id = pt.payment_type_id',\
    get_connection('telco_churn'))