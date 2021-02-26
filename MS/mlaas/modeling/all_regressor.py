'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 Mann Purohit         02-FEB-2021           1.1           

*/
'''

import pandas as pd
import numpy as np
import json
import mlflow
import mlflow.sklearn
import uuid 
import logging
# from database import *



# ## Get Database Connection
# DBObject=db.DBClass()     
# connection,connection_string=DBObject.database_connection(database,user,password,host,port) 

# # get dataset,project,user ids

# sql_command = "select * from mlaas.model_dataset_tbl"

# model_dataset_df=DBObject.select_records(connection,sql_command)
# model_dataset_records=model_dataset_df.to_records(index=False)

# project_id,dataset_id,user_id = model_dataset_records[0]


# Get data dataset info

def get_dataset_ids(**kwargs):
    print("project id")
    print("dataset id")
    print("user id")
    
def get_dataset_info(**kwargs):
    print("still in process")





