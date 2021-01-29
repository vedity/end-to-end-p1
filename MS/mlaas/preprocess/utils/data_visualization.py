# from scipy import stats
# from common.utils.exception_handler.python_exception.common.common_exception import *
# from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *
# from common.utils.database import db
# from common.utils.database.db import DBClass
# from ingest.utils.dataset import dataset_creation
# import logging
# import math
# import pandas as pd
# import numpy as np
# import json
# from ingest.utils.dataset import dataset_creation
# from common.utils.database import db
# from common.utils.database.db import DBClass
# from preprocess.utils.preprocessing import PreprocessingClass
# from .Exploration import dataset_exploration as de

# # dc = dataset_creation.DatasetClass()
# # conn = PreprocessingClass(de.ExploreClass)
# # DBObject,connection,connection_string = conn.get_db_connection()
# class VisualizationClass:

#     def get_data_visualization(self):
#         dataset_id = 260
#         table_name,_,_ = dc.make_dataset_schema()
        
#         #? Getting user_name and dataset_vaisibility
#         sql_command = f"SELECT DATASET_TABLE_NAME FROM {table_name} WHERE DATASET_ID = '{dataset_id}'"
#         visibility_df = DBObject.select_records(connection,sql_command) 

#         dataset_table_name = visibility_df['dataset_table_name'][0]
#         sql_command = f"SELECT * FROM {user_name}.{dataset_table_name}"
#         data_df = DBObject.select_records(connection,sql_command)
        
#         return data_df