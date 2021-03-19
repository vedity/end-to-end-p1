
#* Importing Libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# Exceptions class
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *

from ..schema import schema_creation
import pandas as pd
import logging

sc = schema_creation.SchemaClass()
class EncodeClass:

    
    # def label_encoding(self, series):

    #     labelencoder = LabelEncoder()

    #     series = labelencoder.fit_transform(series)
        
    #     return series

    def label_encoding(self,DBObject,connection,column_list, table_name):
        '''
        Encoding Related Functions.
        '''
        try:
            sql_command = f'update {table_name} m SET "{column_list[1]}" = WANT_THIS from (SELECT  index, dense_rank() OVER ( ORDER BY "{column_list[1]}") AS WANT_THIS FROM {table_name}) s where m."{column_list[0]}" = s."{column_list[0]}";'
            status = DBObject.update_records(connection,sql_command)
            return status

        except Exception as exc:
            return exc
        
    # def one_hot_encoding(self, series):
        
    #     df = pd.DataFrame(series)
    #     col_name = series.name
    
    #     enc = OneHotEncoder(handle_unknown='ignore')

    #     ohe_df = enc.fit_transform(df).toarray()
    #     enc_df = pd.DataFrame(ohe_df, columns = [f"{col_name}_{i}" for i in range(ohe_df.shape[1])])

    #     return enc_df

    def one_hot_encoding(self,DBObject,connection,column_list, table_name, schema_id): 
        '''This function do one-hot-encoding finds the distinct value and append columns with binary values
        '''
        try:
            logging.info("data preprocessing : EncodeClass : one_hot_encoding : execution start")
            value = []
            
            sql_command = f'select distinct "{column_list[1]}" from {table_name} dcat where "{column_list[1]}" is not null'
            df = DBObject.select_records(connection,sql_command)

            
            if len(df[column_list[1]].to_list()) > 5:
                raise EcondingFailed(500) 
            
            for val in range(len(df)):
                value = df.loc[val, {column_list[1]}]
                value1 = "'"+str(value[0])+"'"
                sql_command = f'alter table {table_name} add COLUMN "{value[0]}" text'
                status1 = DBObject.update_records(connection,sql_command)
                sql_command_update=f'update {table_name} m SET "{value[0]}" = WANT_THIS from (SELECT {column_list[0]},case when "{column_list[1]}"={value1} then 1 else 0 END AS WANT_THIS FROM {table_name} )s where m."{column_list[0]}" = s.{column_list[0]}'
                status = DBObject.update_records(connection,sql_command_update)
                schema_update = sc.update_dataset_schema(DBObject,connection,schema_id,[value[0]],['numeric'],missing_flag=['False'],noise_flag=['False'],flag = True)
            
            drop_column = f'ALTER TABLE {table_name} DROP COLUMN "{column_list[1]}";'
            status = DBObject.update_records(connection,drop_column)
            
            schema_delete = sc.delete_schema_record(DBObject,connection,schema_id,column_list[1])

            logging.info("data preprocessing : EncodeClass : one_hot_encoding : execution stop")
            return status

        except (EcondingFailed) as exc:
            logging.error(str(exc.msg)+ " checking")
            return exc.msg
