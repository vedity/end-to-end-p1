
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
        """This function performs label encoding convert the column into numeric value.

        Args:
            DBObject (obj): [database object]
            connection (string): connection with database
            table_name (string): On which table encoding will perform
            column_list (list): column list on which encoding should perform
        Returns:
            Int: [0 : if columns updated, 1 : if column not updated]
        """
        try:
            logging.info("Preprocess : EncodeClass : label_encoding : execution start")
            sql_command = f'update {table_name} m SET "{column_list[1]}" = WANT_THIS from (SELECT  "{column_list[0]}", dense_rank() OVER ( ORDER BY "{column_list[1]}") AS WANT_THIS FROM {table_name}) s where m."{column_list[0]}" = s."{column_list[0]}";'
            status = DBObject.update_records(connection,sql_command)
            logging.info("Preprocess : EncodeClass : label_encoding : execution end")
            return status

        except Exception as exc:
            logging.info("Preprocess : EncodeClass : label_encoding : exception raise "+str(exc))
            return exc
        
    # def one_hot_encoding(self, series):
    #     df = pd.DataFrame(series)
    #     col_name = series.name
    #     enc = OneHotEncoder(handle_unknown='ignore')
    #     ohe_df = enc.fit_transform(df).toarray()
    #     enc_df = pd.DataFrame(ohe_df, columns = [f"{col_name}_{i}" for i in range(ohe_df.shape[1])])
    #     return enc_df

    def one_hot_encoding(self,DBObject,connection,column_list, table_name, schema_id): 
        """This function do one-hot-encoding finds the distinct value and append columns with binary values
        Returns:
            Succesfull:
                Int: [0 : if columns updated, 1 : if column not updated]
            Unsuccessfull :
                Raise exception
        """
        try:
            logging.info("data preprocessing : EncodeClass : one_hot_encoding : execution start")
            value = []
            flag = False
            df = self.select_distinct(DBObject,connection,column_list, table_name)
            if len(df)<10:
                flag = False
            else:
                flag = True
            
            dist_val,alter_val,select_val,val_list,dtype,missing_lst,noise_lst = self.query_string( df,DBObject,connection,table_name,column_list,flag)
        
            alter_col = self.add_column(DBObject,connection,table_name,alter_val)
            
            status = self.update_column(DBObject,connection,table_name,dist_val,column_list,select_val)
            schema_update = sc.update_dataset_schema(DBObject,connection,schema_id,val_list,dtype,missing_flag=missing_lst,noise_flag=noise_lst,flag = True)
            
            status = self.drop_column(DBObject,connection,table_name,column_list)
            schema_delete = sc.delete_schema_record(DBObject,connection,schema_id,column_list[1])          
            logging.info("data preprocessing : EncodeClass : one_hot_encoding : execution stop")
            return status

        except (EcondingFailed) as exc:
            logging.info("data preprocessing : EncodeClass : one_hot_encoding : exception "+str(exc.msg))
            return exc.msg

    def select_distinct(self,DBObject,connection,column_list,table_name):
        """This function will fetch all the unique value in column.

        Args:
            DBObject (obj): [database object]
            connection (string): connection with database
            table_name (string): On which table encoding will perform
            column_list (list): column list on which encoding should perform
        Returns:
            dataframe: List of all distinct value in column.
        """
        try:
            logging.info("Preprocess : EncodeClass : select_distinct : execution start")
            sql_command = f'select distinct "{column_list[1]}" from {table_name} dcat where "{column_list[1]}" is not null'
            df = DBObject.select_records(connection,sql_command)
            logging.info("Preprocess : EncodeClass : select_distinct : execution stop")
            return df
        
        except (EcondingFailed) as exc:
            logging.info("data preprocessing : EncodeClass : one_hot_encoding : exception "+str(exc.msg))
            return exc.msg

    def query_string(self, df,DBObject,connection,table_name,column_list,flag):
        """This function will generate dynamic query string for sql

        Args:
            df (dataframe): list of all disting value in column
            DBObject (obj): [database object]
            connection (string): connection with database
            table_name (string): On which table encoding will perform
            column_list (list): column list on which encoding should perform
            flag (boolean): [True: if more then 10 distinct value, False : if less then 10 distinct value]

        Returns:
            string: returns all query string
        """
        try:
            logging.info("Preprocess : EncodeClass : query_string : execution start")
            #? Initialization of list and string
            dist_val = ""
            select_val = ""
            alter_val = ""
            val_list = []
            dtype = []
            missing_lst = []
            noise_lst = []
            freq_lst = []

            #? [If] distinct value < 10 [else] value < 10
            if flag == False:

                for val in range(len(df)):
                    value = df.loc[val, {column_list[1]}]

                    #? Getting new Col name i.e(colnm_distintvalue)
                    new_col_name = str(column_list[1]) +"_"+ str(value[0])
                    
                    value1 = "'"+str(value[0])+"'"
                    val_list.append(str(new_col_name)) 
                    dtype.append('numeric')
                    missing_lst.append('False')
                    noise_lst.append('False') 

                    #? Dynamic query string for distinct_value,alter_col,select_col
                    dist_val += f'"{new_col_name}"=col{val},'
                    alter_val += f'add COLUMN "{new_col_name}" int,'
                    select_val += f',case when "{column_list[1]}"={value1} then 1 else 0 END AS col{val}'
            else:
                most_occure = self.frequent_value(DBObject,connection,table_name,column_list) #? Most 10 freq distinct value
                
                for val in range(len(most_occure)):
                    value = most_occure.loc[val, {column_list[1]}]
                    
                    #? Getting new Col name
                    new_col_name = str(column_list[1]) +"_"+ str(value[0])
                    
                    value1 = "'"+str(value[0])+"'"
                    freq_lst.append(value[0])
                    val_list.append(str(new_col_name))
                    dtype.append('numeric')
                    missing_lst.append('False')
                    noise_lst.append('False') 

                    #? Dynamic query string for distinct_value,alter_col,select_col
                    dist_val += f'"{new_col_name}"=col{val},'
                    alter_val += f'add COLUMN "{new_col_name}" int,'
                    select_val += f',case when "{column_list[1]}"={value1} then 1 else 0 END AS col{val}'
                
                #? To add column OTHER if more then 10 distinct value
                freq_lst = str(freq_lst)[1:-1]
                dist_val += f'"{column_list[1]}_other"=col,'
                alter_val += f'add COLUMN "{column_list[1]}_other" int,'
                select_val += f', case when "{column_list[1]}" not in ({freq_lst}) then 1 else 0 END AS col'
                val_list.append(f"{column_list[1]}_other")
                dtype.append('numeric')
                missing_lst.append('False')
                noise_lst.append('False') 

            dist_val = dist_val[:len(dist_val)-1]  #? Remove , in dynamic query string
            alter_val = alter_val[:len(alter_val)-1]  #? Remove , in dynamic query string
            
            logging.info("Preprocess : EncodeClass : query_string : execution stop")
            return dist_val,alter_val,select_val,val_list,dtype,missing_lst,noise_lst           

        except (EcondingFailed) as exc:
            logging.info("data preprocessing : EncodeClass : query_string : exception "+str(exc.msg))
            return exc.msg

    def add_column(self,DBObject,connection,table_name,alter_val):
        """This function will add column with all distinct value 

        Args:
            DBObject (obj): [database object]
            connection (string): connection with database
            table_name (string): On which table encoding will perform
            alter_val (list): List of value alter column in tbl.

        Returns:
            Int: [0 : if columns updated, 1 : if column not updated]
        """
        try:
            logging.info("Preprocess : EncodeClass : add_column : execution start")
            sql_command = f'Alter table {table_name} {alter_val}'
            status = DBObject.update_records(connection,sql_command)
            logging.info("Preprocess : EncodeClass : add_column : execution stop")
            return status
        
        except (EcondingFailed) as exc:
            logging.info("data preprocessing : EncodeClass : add_column : exception "+str(exc.msg))
            return exc.msg

    def update_column(self,DBObject,connection,table_name,dist_val,column_list,select_val):
        """This function will update the column with 0 1 value

        Args:
            DBObject (obj): [database object]
            connection (string): connection with database
            table_name (string): On which table encoding will perform
            dist_val (list): Distinct value list from column
            column_list (list): column list on which encoding should perform
            select_val (list): Selected value list

        Returns:
            Int: [0 : if columns updated, 1 : if column not updated]
        """
        try:
            logging.info("Preprocess : EncodeClass : update_column : execution start")
            sql_command_update=f'update {table_name} m SET {dist_val} from (SELECT {column_list[0]} {select_val} FROM {table_name} )s where m."{column_list[0]}" = s.{column_list[0]}'  
            status = DBObject.update_records(connection,sql_command_update)
            logging.info("Preprocess : EncodeClass : update_column : execution stop")
            return status

        except (EcondingFailed) as exc:
            logging.info("data preprocessing : EncodeClass : update_column : exception "+str(exc.msg))
            return exc.msg

   
    def drop_column(self,DBObject,connection,table_name,column_list):
        
        """ This function will drop the original column on which one-hot-encoding is performed.
            Args:
            DBObject (obj): [database object]
            connection (string): [connection with database]
            table_name (string): [On which table encoding will perform]
            column_list (list): [column list on which encoding should perform]
            Returns:
            Int: [0 : if columns updated, 1 : if column not updated]
        """
        try:
            logging.info("Preprocess : EncodeClass : drop_column : execution start")
            drop_column = f'ALTER TABLE {table_name} DROP COLUMN "{column_list[1]}";'
            status = DBObject.update_records(connection,drop_column)   
            logging.info("Preprocess : EncodeClass : drop_column : execution stop") 
            return status

        except (EcondingFailed) as exc:
            logging.info("data preprocessing : EncodeClass : drop_column : exception "+str(exc.msg))
            return exc.msg
    

    def frequent_value(self,DBObject,connection,table_name,column_list):
        """This function will return list of top 10 values which is most occuring.
            DBObject (obj): [database object]
            connection (string): [connection with database]
            table_name (string): [On which table encoding will perform]
            column_list (list): [column list on which encoding should perform]
            Returns:
                List of all 10 most occuring values.
        """
        try:
            logging.info("Preprocess : EncodeClass : frequent_value : execution start")
            sql_command = f'SELECT  "{column_list[1]}",count(*) from {table_name} GROUP BY "{column_list[1]}" order by count(*)  desc limit  10;'
            freq_val = DBObject.select_records(connection,sql_command)
            logging.info("Preprocess : EncodeClass : frequent_value : execution stop")
            return freq_val
        
        except (EcondingFailed) as exc:
            logging.info("data preprocessing : EncodeClass : frequent_value : exception "+str(exc.msg))
            return exc.msg