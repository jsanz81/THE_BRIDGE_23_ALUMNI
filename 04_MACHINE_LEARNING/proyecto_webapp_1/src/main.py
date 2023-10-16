'''
Name: main.py
Version: 1.0
Description:
Release_date:
Updated_date:
Author:

'''
import os, sys
import logging
import pandas as pd
#import utils.custom_functions as f

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir))

print(PROJECT_ROOT)

data_folder = (PROJECT_ROOT + "\\" + "dataset")
print(data_folder)

## Cargando las variables de entorno
# f.get_args()

# environment = f.options.env
# print(environment)

# data_source = f.options.data_source
# print(data_source)

# db_table_name = f.options.dbtable

# Configuramos el formato del logger
FORMAT = '%(asctime)-15s - %(message)s'
logging.basicConfig(format=FORMAT
                    ,level=logging.INFO
                    ,filemode='w'
                    )
logger = logging.getLogger("main.py")
logger.setLevel("INFO")

# def main():
#     for df in df_list:
#         df['Weight_new'] = df['Weight'].apply(f.remove_kg)
#         print(df['Weight'])
    
    

if __name__ == '__main__':
    logger.info("--- Script start ---")
    #main()
    logger.info("--- Script end ---")