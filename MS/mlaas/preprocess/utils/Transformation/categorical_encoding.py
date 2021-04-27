'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Nisha Barad         27-Feb-2021           1.0            EncodeClass
 
*/
'''

#* Library Imports
import pandas as pd
import logging

#* Importing Libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# Exceptions class
from common.utils.exception_handler.python_exception.preprocessing.preprocess_exceptions import *

#* Relative Imports
from ..schema import schema_creation

#* Defining Objects
sc = schema_creation.SchemaClass()

class EncodeClass:

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
            logging.info("data preprocess : EncodeClass : label_encoding : execution start")
            
            #Update records with specific integer value in sequence.
            sql_command = f'update {table_name} m SET "{column_list[1]}" = WANT_THIS from (SELECT  "{column_list[0]}", dense_rank() OVER ( ORDER BY "{column_list[1]}") AS WANT_THIS FROM {table_name}) s where m."{column_list[0]}" = s."{column_list[0]}";'
            status = DBObject.update_records(connection,sql_command)

            #Convert updated column datatype to Integer
            update_dtype_sql_command = f'ALTER TABLE {table_name} ALTER COLUMN "{column_list[1]}" type "int8" USING "{column_list[1]}"::bigint;'
            status = DBObject.update_records(connection,update_dtype_sql_command)

            logging.info("data preprocess : EncodeClass : label_encoding : execution end")
            return status

        except Exception as e:
            logging.info("data preprocess : EncodeClass : label_encoding : execution failed "+str(e))
            logging.info("data preprocess : EncodeClass : label_encoding : execution failed "+traceback.format_exc())
            return 1
        
 
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
            #false flag indicates column having less then 10 distinct value
            flag = False 

            #fetch all distinct value in particular column
            df = self.select_distinct(DBObject,connection,column_list, table_name)

            #check if distinct value less then 10 flag=false else flag=true
            if len(df)<10:
                flag = False
            else:
                flag = True
            
            #Dynamic query func call
            dist_val,alter_val,select_val,val_list,dtype,missing_lst,noise_lst = self.query_string( df,DBObject,connection,table_name,column_list,flag)
        
            #Alter column with distinct name
            alter_col = self.add_column(DBObject,connection,table_name,alter_val)
            
            #Update column with 0 1 value if value exists then 1 else 0
            status = self.update_column(DBObject,connection,table_name,dist_val,column_list,select_val)
            schema_update = sc.update_dataset_schema(DBObject,connection,schema_id,val_list,dtype,missing_flag=missing_lst,noise_flag=noise_lst,flag = True)
            
            #Drop original column after encoding
            status = self.drop_column(DBObject,connection,table_name,column_list)
            schema_delete = sc.delete_schema_record(DBObject,connection,schema_id,column_list[1])  

            logging.info("data preprocessing : EncodeClass : one_hot_encoding : execution stop")
            return status

        except (EcondingFailed) as e:
            logging.info("data preprocessing : EncodeClass : one_hot_encoding : execution failed "+str(e))
            logging.info("data preprocessing : EncodeClass : one_hot_encoding : execution failed "+traceback.format_exc())
            return 1

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
            
            #Select distinct value from particular row
            sql_command = f'select distinct "{column_list[1]}" from {table_name} dcat where "{column_list[1]}" is not null'
            df = DBObject.select_records(connection,sql_command)
            
            logging.info("data preprocess : EncodeClass : select_distinct : execution stop")
            return df
        
        except (EcondingFailed) as e:
            logging.info("data preprocessing : EncodeClass : select_distinct : execution failed "+str(e))
            logging.info("data preprocessing : EncodeClass : select_distinct : execution failed "+traceback.format_exc())
            return 1

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
            logging.info("data preprocess : EncodeClass : query_string : execution start")

            # Initialization of list and string
            dist_val = ""
            select_val = ""
            alter_val = ""
            val_list = []
            dtype = []
            missing_lst = []
            noise_lst = []
            freq_lst = []

            # [If] distinct value < 10 [else] value < 10
            if flag == False:

                for val in range(len(df)):
                    value = df.loc[val, {column_list[1]}]

                    # Getting new Col name i.e(colnm_distintvalue)
                    new_col_name = str(column_list[1]) +"_"+ str(value[0])
                    
                    value1 = "'"+str(value[0])+"'"
                    val_list.append(str(new_col_name)) 
                    dtype.append('numeric')
                    missing_lst.append('False')
                    noise_lst.append('False') 

                    # Dynamic query string for distinct_value,alter_col,select_col
                    dist_val += f'"{new_col_name}"=col{val},'
                    alter_val += f'add COLUMN "{new_col_name}" int,'
                    select_val += f',case when "{column_list[1]}"={value1} then 1 else 0 END AS col{val}'
            else:
                most_occure = self.frequent_value(DBObject,connection,table_name,column_list) # Most 10 freq distinct value
                
                for val in range(len(most_occure)):
                    value = most_occure.loc[val, {column_list[1]}]
                    
                    # Getting new Col name
                    new_col_name = str(column_list[1]) +"_"+ str(value[0])
                    
                    value1 = "'"+str(value[0])+"'"
                    freq_lst.append(value[0])
                    val_list.append(str(new_col_name))
                    dtype.append('numeric')
                    missing_lst.append('False')
                    noise_lst.append('False') 

                    # Dynamic query string for distinct_value,alter_col,select_col
                    dist_val += f'"{new_col_name}"=col{val},'
                    alter_val += f'add COLUMN "{new_col_name}" int,'
                    select_val += f',case when "{column_list[1]}"={value1} then 1 else 0 END AS col{val}'
                
                # To add column OTHER if more then 10 distinct value
                freq_lst = str(freq_lst)[1:-1]
                dist_val += f'"{column_list[1]}_other"=col,'
                alter_val += f'add COLUMN "{column_list[1]}_other" int,'
                select_val += f', case when "{column_list[1]}" not in ({freq_lst}) then 1 else 0 END AS col'
                val_list.append(f"{column_list[1]}_other")
                dtype.append('numeric')
                missing_lst.append('False')
                noise_lst.append('False') 

            dist_val = dist_val[:len(dist_val)-1]  # Remove , in dynamic query string
            alter_val = alter_val[:len(alter_val)-1]  # Remove , in dynamic query string
            
            logging.info("data preprocess : EncodeClass : query_string : execution stop")
            return dist_val,alter_val,select_val,val_list,dtype,missing_lst,noise_lst           

        except (EcondingFailed) as e:
            logging.info("data preprocessing : EncodeClass : query_string : execution failed "+str(e))
            logging.info("data preprocessing : EncodeClass : query_string : execution failed "+traceback.format_exc())
            return 1

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
            logging.info("data preprocess : EncodeClass : add_column : execution start")

            #Alter table with new columns 
            sql_command = f'Alter table {table_name} {alter_val}'
            status = DBObject.update_records(connection,sql_command)

            logging.info("data preprocess : EncodeClass : add_column : execution stop")
            return status
        
        except (EcondingFailed) as e:
            logging.info("data preprocessing : EncodeClass : add_column : execution failed "+str(e))
            logging.info("data preprocessing : EncodeClass : add_column : execution failed "+traceback.format_exc())
            return 1

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
            logging.info("data preprocess : EncodeClass : update_column : execution start")
            
            #Update new columns with 0 or 1, if value exists then 1 else 0
            sql_command_update=f'update {table_name} m SET {dist_val} from (SELECT {column_list[0]} {select_val} FROM {table_name} )s where m."{column_list[0]}" = s.{column_list[0]}'  
            status = DBObject.update_records(connection,sql_command_update)
            
            logging.info("data preprocess : EncodeClass : update_column : execution stop")
            return status

        except (EcondingFailed) as e:
            logging.info("data preprocessing : EncodeClass : update_column : execution failed "+str(e))
            logging.info("data preprocessing : EncodeClass : update_column : execution failed "+traceback.format_exc())
            return 1

   
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
            logging.info("data preprocess : EncodeClass : drop_column : execution start")
            
            #Drop original column 
            drop_column = f'ALTER TABLE {table_name} DROP COLUMN "{column_list[1]}";'
            status = DBObject.update_records(connection,drop_column)   
            
            logging.info("data preprocess : EncodeClass : drop_column : execution stop") 
            return status

        except (EcondingFailed) as e:
            logging.info("data preprocessing : EncodeClass : drop_column : execution failed "+str(e))
            logging.info("data preprocessing : EncodeClass : drop_column : execution failed "+traceback.format_exc())
            return 1
    

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
            logging.info("data preprocess : EncodeClass : frequent_value : execution start")
            
            #Fetch most frequent 10 column values
            sql_command = f'SELECT  "{column_list[1]}",count(*) from {table_name} GROUP BY "{column_list[1]}" order by count(*)  desc limit  10;'
            freq_val = DBObject.select_records(connection,sql_command)
            
            logging.info("data preprocess : EncodeClass : frequent_value : execution stop")
            return freq_val
        
        except (EcondingFailed) as e:
            logging.info("data preprocessing : EncodeClass : frequent_value : execution failed "+str(e))
            logging.info("data preprocessing : EncodeClass : frequent_value : execution failed "+traceback.format_exc())
            return 1

    # def get_unencoded_colnames(self,DBObject,connection,project_id):
    #     '''
    #         Used to get the names of all the columns that are yet to be encoded.

    #         Args:
    #         ----
    #         DBObject (`object`): DB Class Object.
    #         connection (`object`): Postgres connection object.
    #         project_id (`int`): Id of the project

    #         Returns:
    #         -------
    #         flag (`boolean`): Is any encoding remaining or not
    #         description (`String`): The message that will be shown in the front end.
    #     '''
    #     try:
    #         logging.info("data preprocessing : EncodeClass : get_unencoded_colnames : execution start")

    #         sql_command = f"""SELECT column_name 
    #                     FROM INFORMATION_SCHEMA.columns 
    #                     where table_name = (select dt.dataset_table_name 
    #                                             from mlaas.project_tbl pt, mlaas.dataset_tbl dt 
    #                                             where pt.project_id = '{project_id}' 
    #                                             and dt.dataset_id = pt.dataset_id
    #                                             ) 
    #                     and data_type='text'
    #                     and column_name not in (
    #                         select 
    #                             case
    #                                 when st.changed_column_name = null
    #                                     then st.column_name 
    #                                 else
    #                                     st.changed_column_name 
    #                             end
    #                         from mlaas.schema_tbl st 
    #                         where st.schema_id = (select pt2.schema_id 
    #                                                 from mlaas.project_tbl pt2 
    #                                                 where pt2.project_id = '{project_id}'
    #                                                 ) 
    #                         and st.column_attribute in ('Target','Ignore')
    #                     )
    #                     """
            
    #         unencoded_cols_df = DBObject.select_records(connection,sql_command)
            
    #         if not isinstance(unencoded_cols_df,pd.DataFrame):
    #             raise TypeError
            
        #     #? Sub Function for getting column names
        #     def get_unencoded_desc(df,col_name):
        #         '''
        #             This is a sub-function thats specifically used to get the message for 
        #             unencoded columns list. This message will be shown on the frontend.

        #             Args:
        #             ----
        #             df (`pd.DataFrame`): Dataframe containing unencoded column_names in a single column.
        #             col_name (`String`): Name of the column that contains the unencoded column names.

        #             Returns:
        #             -------
        #             string (`String`): Description for unencoded column warning.
        #         '''
        #         logging.info("data preprocessing : EncodeClass : get_unencoded_desc : execution start")

        #         if len(df) == 0:
        #             string = "No column remaining for Categorical Encoding."
        #         else:    
        #             string = "Categorical Encoding Remaining in Columns "

        #             #? Adding column names
        #             for i,data in df.iterrows():
        #                 string += f"'{data[col_name]}', "
        #             else:
        #                 string = string[:-2]+"."
                
        #         logging.info("data preprocessing : EncodeClass : get_unencoded_desc : execution stop")

        #         return string

        #     logging.info("data preprocessing : EncodeClass : get_unencoded_colnames : execution stop")

        #     if len(unencoded_cols_df) == 0:
        #         #? No unencoded columns remaining in the dataset
        #         return True, get_unencoded_desc(unencoded_cols_df,'column_name')
        #     else:
        #         #? Some unencoded columns are still remaining in the dataset.
        #         return False, get_unencoded_desc(unencoded_cols_df,'column_name')

        # except Exception as e:
        #     logging.error(f"data preprocessing : EncodeClass : get_unencoded_colnames : function failed : {str(e)}")
        #     return False, str(e)
        
