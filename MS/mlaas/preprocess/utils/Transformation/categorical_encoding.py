
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
            sql_command = f'update {table_name} m SET "{column_list[1]}" = WANT_THIS from (SELECT  "{column_list[0]}", dense_rank() OVER ( ORDER BY "{column_list[1]}") AS WANT_THIS FROM {table_name}) s where m."{column_list[0]}" = s."{column_list[0]}";'
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
        sql_command = f'select distinct "{column_list[1]}" from {table_name} dcat where "{column_list[1]}" is not null'
        df = DBObject.select_records(connection,sql_command)
        return df

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
        dist_val = ""
        select_val = ""
        alter_val = ""
        val_list = []
        dtype = []
        missing_lst = []
        noise_lst = []
        if flag == False:
            for val in range(len(df)):
                value = df.loc[val, {column_list[1]}]

                #? Getting new Col name
                new_col_name = column_list[1] +"_"+ value[0]
                
                value1 = "'"+str(value[0])+"'"
                val_list.append(str(new_col_name))
                dtype.append('numeric')
                missing_lst.append('False')
                noise_lst.append('False') 
                dist_val += f'"{new_col_name}"=col{val},'
                alter_val += f'add COLUMN "{new_col_name}" int,'
                select_val += f',case when "{column_list[1]}"={value1} then 1 else 0 END AS col{val}'
        else:
            most_occure = self.frequent_value(DBObject,connection,table_name,column_list)
            logging.info(" checking "+str(most_occure))
            for val in range(len(most_occure)):
                value = most_occure.loc[val, {column_list[1]}]
                
                #? Getting new Col name
                new_col_name = column_list[1] +"_"+ value[0]
                
                value1 = "'"+str(value[0])+"'"
                val_list.append(str(new_col_name))
                dtype.append('numeric')
                missing_lst.append('False')
                noise_lst.append('False') 
                dist_val += f'"{new_col_name}"=col{val},'
                alter_val += f'add COLUMN "{new_col_name}" int,'
                select_val += f',case when "{column_list[1]}"={value1} then 1 else 0 END AS col{val}'
            
            freq_lst = str(val_list)[1:-1]
            dist_val += f'"{column_list[1]}_other"=col,'
            alter_val += f'add COLUMN "{column_list[1]}_other" int,'
            select_val += f', case when "{column_list[1]}" not in ({freq_lst}) then 1 else 0 END AS col'
            val_list.append(f"{column_list[1]}_other")
            dtype.append('numeric')
            missing_lst.append('False')
            noise_lst.append('False') 
        dist_val = dist_val[:len(dist_val)-1]
        alter_val = alter_val[:len(alter_val)-1]
        
        return dist_val,alter_val,select_val,val_list,dtype,missing_lst,noise_lst

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
        sql_command = f'Alter table {table_name} {alter_val}'
        status = DBObject.update_records(connection,sql_command)
        return status

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
        sql_command_update=f'update {table_name} m SET {dist_val} from (SELECT {column_list[0]} {select_val} FROM {table_name} )s where m."{column_list[0]}" = s.{column_list[0]}'  
        
        logging.info("------->UP "+sql_command_update)
        status = DBObject.update_records(connection,sql_command_update)
        return status

   
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
        drop_column = f'ALTER TABLE {table_name} DROP COLUMN "{column_list[1]}";'
        status = DBObject.update_records(connection,drop_column)    
        return status

    

    def frequent_value(self,DBObject,connection,table_name,column_list):
        """This function will return list of top 10 values which is most occuring.
            DBObject (obj): [database object]
            connection (string): [connection with database]
            table_name (string): [On which table encoding will perform]
            column_list (list): [column list on which encoding should perform]
            Returns:
                List of all 10 most occuring values.
        """
        sql_command = f'SELECT  "{column_list[1]}",count(*) from {table_name} GROUP BY "{column_list[1]}" order by count(*)  desc limit  10;'
        logging.info("------->FRQ "+sql_command)
        freq_val = DBObject.select_records(connection,sql_command)
        return freq_val

    def get_unencoded_colnames(self,DBObject,connection,project_id):
        '''
            Used to get the names of all the columns that are yet to be encoded.

            Args:
            ----
            DBObject (`object`): DB Class Object.
            connection (`object`): Postgres connection object.
            project_id (`int`): Id of the project

            Returns:
            -------
            flag (`boolean`): Is any encoding remaining or not
            description (`String`): The message that will be shown in the front end.
        '''
        try:
            logging.info("data preprocessing : EncodeClass : get_unencoded_colnames : execution start")

            sql_command = f"select dt.dataset_table_name from mlaas.project_tbl pt, mlaas.dataset_tbl dt where pt.project_id = '{project_id}' and dt.dataset_id = pt.dataset_id"
            table_name_df = DBObject.select_records(connection,sql_command)
            
            if not isinstance(table_name_df,pd.DataFrame):
                raise TypeError

            table_name = table_name_df['dataset_table_name'][0]

            sql_command = f"SELECT column_name FROM INFORMATION_SCHEMA.columns where table_name= '{table_name}' and data_type='text'"
            unencoded_cols_df = DBObject.select_records(connection,sql_command)
            
            if not isinstance(unencoded_cols_df,pd.DataFrame):
                raise TypeError
            
            #? Sub Function for getting column names
            def get_unencoded_desc(df,col_name):
                '''
                    This is a sub-function thats specifically used to get the message for 
                    unencoded columns list. This message will be shown on the frontend.

                    Args:
                    ----
                    df (`pd.DataFrame`): Dataframe containing unencoded column_names in a single column.
                    col_name (`String`): Name of the column that contains the unencoded column names.

                    Returns:
                    -------
                    string (`String`): Description for unencoded column warning.
                '''
                logging.info("data preprocessing : EncodeClass : get_unencoded_desc : execution start")

                if len(df) == 0:
                    string = "No column remaining for Categorical Encoding."
                else:    
                    string = "Categorical Encoding Remaining in Columns "

                    #? Adding column names
                    for i,data in df.iterrows():
                        string += f"'{data[col_name]}', "
                    else:
                        string = string[:-2]+"."

                logging.info("data preprocessing : EncodeClass : get_unencoded_desc : execution stop")

                return string

            logging.info("data preprocessing : EncodeClass : get_unencoded_colnames : execution stop")

            if len(unencoded_cols_df) == 0:
                #? No unencoded columns remaining in the dataset
                return True, get_unencoded_desc(unencoded_cols_df,'column_name')
            else:
                #? Some unencoded columns are still remaining in the dataset.
                return False, get_unencoded_desc(unencoded_cols_df,'column_name')

        except Exception as e:
            logging.error(f"data preprocessing : EncodeClass : get_unencoded_colnames : function failed : {str(e)}")
            return False, str(e)
