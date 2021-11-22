import pandas as pd
import os


def get_connection(db_name):
    '''
   This function used the passed database name and imports host, user, password
   from the locally saved env file to authenticate with the MySQL server.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


def new_telco():
    '''
    This function uses the get_connection function to pull the fall tables from the
    telco_churn database: customers, contract_type, internet_service_types, payment_types
    This function will then create a dataframe from those tables.
        '''
    sql = '''
        SELECT * FROM customers c
        JOIN contract_types ct ON ct.contract_type_id=c.contract_type_id
        JOIN internet_service_types ist ON ist.internet_service_type_id=c.internet_service_type_id
        JOIN payment_types pt ON pt.payment_type_id=c.payment_type_id
        '''
    url = get_connection('telco_churn')
    df = pd.read_sql(sql, url)


def get_telco():
    '''
    This fuction uses the the get_telco function to pull the telco data from the server and save it locally
    as a csv file or read it from an already saved csv file
    '''
    file_name = 'telco.csv'
    if os.path.isfile(file_name):
        df = pd.read_csv(file_name, index_col=0)
    else:
        df = get_telco()
        df.to_csv(file_name)
    return df  
    