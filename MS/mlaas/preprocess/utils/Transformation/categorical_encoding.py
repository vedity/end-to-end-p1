
#* Importing Libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import logging

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

    def one_hot_encoding(self,DBObject,connection,column_list, table_name):
        try:
            value = []
            distinct = []
            sql_command = f'select distinct "{column_list[1]}" from {table_name} dcat where "{column_list[1]}" is not null'
            df = DBObject.select_records(connection,sql_command)
            for val in range(len(df)):
                value = df.loc[val, {column_list[1]}]
                distinct = value[0]
            logging.info("====>"+str(distinct))

            for val in range(len(df)):
                value = df.loc[val, {column_list[1]}]
                value1 = "'"+str(value[0])+"'"
                logging.info("******>"+str(value))
                sql_command = f'select *,case when "{column_list[1]}" = {value1} then 1 else 0 end "{value[0]}" from {table_name}'
                df = DBObject.select_records(connection,sql_command)
                logging.info("----++++>"+str(sql_command))
                logging.info("----++++>"+str(df))
            return df

        except Exception as exc:
            return exc
