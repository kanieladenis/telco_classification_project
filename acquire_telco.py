import pandas as pd



# create function 'get_connection' for repeated use to pass authentication to MySQL server
def get_connection(db_name):
    '''
   This function used the passed database name and imports host, user, password
   from the locally saved env file to authenticate with the MySQL server.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# create function 'get_telco' to pull all records from all tables from telco_churn database..
def get_telco():
    '''
    This function uses the the get_connection function to pull the telco data from the MySQL server. 
    '''
    sql = '''
    SELECT * FROM customers c
    JOIN contract_types ct ON ct.contract_type_id=c.contract_type_id
    JOIN internet_service_types ist ON ist.internet_service_type_id=c.internet_service_type_id
    JOIN payment_types pt ON pt.payment_type_id=c.payment_type_id
    '''
    url = get_connection('telco_churn')
    df = pd.read_sql(sql, url)
    return df
    