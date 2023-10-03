'''
Name: custom_functions.py
Version: 1.0
Description:
Release_date:
Updated_date:
Author:

Release note:
    1.0 - removing bugs...
    0.2beta - ....
    0.1beta - ....
    

'''


# Importamos las librerías de sistema
import sys
import os
import json
import logging

from argparse import ArgumentParser
from datetime import datetime, timezone
from time import sleep
import requests
import pandas as pd
import numpy as np
import sqlite3


#import load_dotenv

# Ruta del sistema

sys.path.append(
    os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir
    ))
)

env_path = os.path.join('setup', '.env')
#load_dotenv(env_path)

# Configuramos el formato del logger
FORMAT = '%(asctime)-15s - %(message)s'
logging.basicConfig(format=FORMAT
                    ,level=logging.INFO
                    ,filemode='w'
                    )
logger = logging.getLogger("main.py")
logger.setLevel("INFO")


# Definimos los argumentos o parámetros 

def get_args():
    '''
    Recogemos los argumentos del script main.py
    '''
    global options
    logger.info("--- Get args initialized ---")
    parser = ArgumentParser(description="Get args from main.py")
    parser.add_argument('--env', default='DEV',
                        choices=['DEV','QA','PRO'], type=str,
                        required=True, help='Please select the environment')
    parser.add_argument('-ds', '--data_source', 
                        default=1, type=int,
                        required=False, help="""
                            Select type of data source:
                        '1' : 'BostonHousing',
                        '2': 'Iris',
                        '3' : 'Titanic'
                        """
                        )
    parser.add_argument('--dbtable', type=str)
    options = parser.parse_args()
    logger.info("--- Get args loaded --- \n")
    
    
class TheBridgeDatabase():
    
    '''
    Creamos la clase TheBridgeDatabase..
    '''
    
    def __init__(self, env):
        '''
        Args:
        ----
            creds_file: from config dictionary values
        Return:
        ------
            credenciales variables for database
        '''
        self.environment = env
        # self.db_endpoint, self.db_port, self.db_name, self.db_schema, self.db_user, self.db_pass = creds_file.values() #noqa
        # self.uri = f'mssql+pymssql://{self.db_user}:{self.db_pass}@{self.db_endpoint}:{self.db_port}/{self.db_name}' #noqa
        # self.engine = create_engine(self.uri)
        print(self.environment)
        logger.info(f"--- {TheBridgeDatabase.__name__} has been initialized ---")
    
    
    def create_database_sqlite(self, path=None):
        self.conn = sqlite3.connect(f'thebridge_dwh_{self.environment}.db')
        cursor = self.conn.cursor()
        with open('src/data/raw/practica_sql_script_erp.sql', 'r') as q:
            sql = q.read()
            cursor.executescript(sql)
        return cursor

    def read_table(self, table_name=None):
        self.tables = pd.read_sql(f""" select *
                            from sqlite_master 
                            where type='table' and
                            name = '{table_name}'
                            order by name;
                            """, self.conn)
        return self.tables


# class DataFrameTransform():
    
#     def __init__(self):
#         pass
    
def remove_kg(row, custom_attr):
    row = row.lower()
    if 'kg' in row:
        return float(row.split('kg')[0])
    else:
        return float(row)
    
def remove_kg(row, custom_attr):
    row = row.lower()
    if 'kg' in row:
        return float(row.split('kg')[0])
    else:
        return float(row)
    
def remove_kg(row, custom_attr):
    row = row.lower()
    if 'kg' in row:
        return float(row.split('kg')[0])
    else:
        return float(row)
    
def remove_kg(row, custom_attr):
    row = row.lower()
    if 'kg' in row:
        return float(row.split('kg')[0])
    else:
        return float(row)
    
def remove_ids(df, ids=None):
    
    global train_ids, test_ids
    
    # Guardamos las IDs de train y test
    train_ids = df_list[0].id.to_list()
    test_ids = df_list[1].id.to_list()
    
    ids = list()
    
    # Eliminamos la Ids
    for df in df_list:
        df.drop('id', axis=1, inplace=True)
    
    # Eliminamos la variable laptop_ID
    for df in df_list:
        df.drop('laptop_ID', axis=1, inplace=True)
    
    return df
    
    

# with open('BBDD_ERP_data.sql', 'r') as q:
#     sql = q.read()
#     cursor.executescript(sql)
    
# pd.read_sql(""" select *
#                         from sqlite_schema
#                         """, conn)

def remove_kg(row, custom_attr):
        row = row.lower()
        if 'kg' in row:
            return float(row.split('kg')[0])
        else:
            return float(row)
        
df['Weight'].apply(remove_kg, custom_attr)