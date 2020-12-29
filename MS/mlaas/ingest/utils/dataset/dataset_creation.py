'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/
 Jay Shukla               15-DEC-2020           1.2           Added Deletion Functionality
 Abhishek Negi            12=DEC-2020           1.3           need to Check the code not working fine
*/
'''
# from mlaas.ingest.utils import dataset
import os
import pandas as pd
from ..project import project_creation

class DatasetClass:
   
    def make_dataset_schema(self):
        """ This function is used to make schema for creating dataset table.

        Returns:
            [string]: [it will return name of the table, structure of the table and columns of the table.]
        """
        # Dataset table name
        table_name = 'mlaas.dataset_tbl' 
        # Columns for dataset table.
        cols = 'dataset_id,dataset_name,file_name,file_size,dataset_table_name,dataset_visibility,user_name' 
        # Schema for dataset table.
        schema = "dataset_id bigserial,"\
                 "dataset_name  text,"\
                 "file_name  text,"\
                 "file_size  text,"\
                 "dataset_table_name  text,"\
                 "dataset_visibility text,"\
                 "user_name  text,"\
                 "created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()"           
        return table_name,schema,cols

    def  make_dataset_records(self,dataset_name,file_name,dataset_visibility,user_name):
        """This function is used to make records for inserting data into table based on input dataframe.
           E.g. column_name_1,column_name_2 .......,column_name_n.

        Args:
            dataset_name ([string]): [name of the dataset.]
            file_name ([string]): [name of the file.]
            dataset_visibility ([string]): [visibility of the dataset.]
            user_name ([string]): [name of the user.]

        Returns:
            [tuple]: [it will return records in the form of tuple.]
        """
        file_path = self.get_file_path(file_name,dataset_visibility,user_name)
        file_size = self.get_file_size(file_path)# Get size of uploaded file.
        dataset_table_name = self.get_dataset_table_name(file_name) # Make table name for loaded csv.
        row=dataset_name,file_name,file_size,dataset_table_name,dataset_visibility,user_name # Make record for dataset table.
        row_tuples = [tuple(row)] # Convert row record into list of tuple.
        return row_tuples
    
    def get_file_path(self,file_name,dataset_visibility,user_name):
        """This function is used to get server file path.

        Args:
            file_name ([string]): [name of the file.]
            dataset_visibility ([string]): [visibility of the dataset.]
            user_name ([string]): [name of the user.]

        Returns:
            [string]: [it will return path of the file.]
        """
        
        if dataset_visibility.lower() == "public" :
            file_path = './static/server/' + dataset_visibility + "/" + file_name
        else:
            file_path = './static/server/' + user_name + "/" + file_name 
        return file_path
    
    def get_file_size(self,file_path):
        """This function is used to get size of the file.

        Args:
            file_path ([string]): [relative path of the file.]

        Returns:
            [string]: [it will return size of the file. in GB or MB or KB.]
        """
            
        
        file_size = os.path.getsize(file_path)
        max_size = 512000
        if file_size < max_size:
            value = round(file_size/1000, 2)
            ext = ' kb'
        elif file_size < max_size * 1000:
            value = round(file_size/1000000, 2)
            ext = ' Mb'
        else:
            value = round(file_size/1000000000, 2)
            ext = ' Gb' 
        return str(value)+ext
    
    def get_dataset_table_name(self,file_name):
        """This function is used to get dataset table name.

        Args:
            file_name ([string]): [name of the file.]

        Returns:
            [string]: [it will return name of the table.]
        """
        
        table_name = ("di_" + file_name.replace(".csv","") + "_" + "tbl").lower()
        return table_name
        
 

    def make_dataset(self,DBObject,connection,dataset_name,file_name,dataset_visibility,user_name):
        """This function is used to main dataset table and also load main dataset details into database table.
           E.g. dataset details : dataset_name,file_name,file_size,dataset_table_name,user_name.

        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            dataset_name ([string]): [name of the dataset.]
            file_name ([string]): [name of the file.]
            dataset_visibility ([string]): [visibility of the dataset.]
            user_name ([string]): [name of the user.]

        Returns:
            [string,integer]: [it will return status of dataset creation. if successfully created then 1 else 0.
                                and also return dataset id of created dataset.]
        """
        schema_status = DBObject.create_schema(connection)
        table_name,schema,cols = self.make_dataset_schema() # Get table name,schema and columns from dataset class.
        
        #? Checking if the same dataset is there for the same user in the dataset table? If yes, then it will not insert a new row in the table
        dataset_exist = self.dataset_exists(DBObject,connection,table_name,dataset_visibility,dataset_name,user_name)
        
        if dataset_exist == False: pass #? No dataset with same name exists so creating the new one
        else: return 2,dataset_exist #? dataset_exists() function returns id of the dataset if dataset with same name exists

        create_status = DBObject.create_table(connection,table_name,schema) # Get status about dataset tableis created or not.if created then 0 else 1.

        row_tuples = self.make_dataset_records(dataset_name,file_name,dataset_visibility,user_name) # Get record for dataset table.
        insert_status = DBObject.insert_records(connection,table_name,row_tuples,cols) # Get status about inserting records into dataset table. if successful then 0 else 1.
        
        # Condition will check dataset table created and data is successfully stored into project table or not.if both successful then 0 else 1. 
        if schema_status in [0,1] and create_status in [0,1] and insert_status == 0 :
            dataset_id = self.get_dataset_id(DBObject,connection,row_tuples,user_name)
            status = 0 # If Successfully.
        else :
            status = 1 # If Failed.
            dataset_id = None

        return status,dataset_id
    
    def load_dataset(self,DBObject,connection,connection_string,file_name,dataset_visibility,user_name):
        """This function is used to load csv file data into database table.

        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            connection_string ([string]): [connection string of the database.]
            file_name ([string]): [name of the file.]
            dataset_visibility ([string]): [visibility of the dataset.]
            user_name ([string]): [name of the user.]

        Returns:
            [type]: [it will return status about loaded data.if successfully then 1 else 0.]
        """
        # Get file relative file path.
        file_path = self.get_file_path(file_name,dataset_visibility,user_name)
        # Get dataframe of the file data.
        file_data_df = DBObject.read_data(file_path)
        # Get table name.
        table_name = self.get_dataset_table_name(file_name)
        # Get schema status.if successfully then 0 else 1.
        schema_status = DBObject.create_schema(connection,user_name)
        # Get load dataset status. if successfully then 0 else 1.
        load_dataset_status = DBObject.load_csv_into_db(connection_string,table_name,file_data_df,user_name)
        return load_dataset_status
    
    def get_dataset_id(self,DBObject,connection,row_tuples,user_name):
        """This function is used to get dataset id of the created dataset.

        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            row_tuples ([list]): [list of the tuple of dataset record.]
            user_name ([string]): [name of the user.]

        Returns:
            [integer]: [it will return dataset id of the created dataset.]
        """
        # Get table name.
        table_name,*_ = self.make_dataset_schema()
        # Get dataset name.
        dataset_name,*_ = row_tuples[0]
        # Prepare select sql command to fetch dataset id from dataset table for particular user.
        sql_command = "SELECT dataset_id from "+ table_name + " Where dataset_name ='"+ dataset_name + "' and user_name = '"+ user_name + "'"
        # Get dataframe of dataset id. 
        dataset_df = DBObject.select_records(connection,sql_command)
        # Get dataset id.
        dataset_id = int(dataset_df['dataset_id'][0])
        return dataset_id

    def show_dataset_details(self,DBObject,connection,user_name):
        """This function is used to show details about all created datasets by user.

        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataset details in the form of dataframe.]
        """
        table_name,_,cols = self.make_dataset_schema() # Get table name,schema and columns from dataset class.
        # This command is used to get dataset details from dataset table of database.
        sql_command = "SELECT "+ cols +" FROM "+ table_name + " WHERE USER_NAME ='"+ user_name +"'"
        dataset_df=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
        return dataset_df

    def show_data_details(self,DBObject,connection,table_name,user_name):
        """This function is used to show details about loaded dataset.

        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            table_name ([string]): [name of the table.]

        Returns:
            [dataframe]: [it will return loaded csv data in the form of dataframe.]
        """
        # This command is used to get data details (i.e. loaded csv file data) from database.
        sql_command = 'SELECT * FROM '+ user_name +'.' + table_name 
        # Get dataframe of loaded csv.
        data_details_df = DBObject.select_records(connection,sql_command) 
        return data_details_df

    #* Version 1.2
    def delete_dataset_details(self,DBObject,connection,dataset_id,user_name,skip_check = False):
        """This function is used to delete dataset entry from the dataset table.

        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            dataset_id ([integer]): [dataset id for the delete dataset record.]

        Returns:
            [integer]: [it will return status of the dataset deletion. if successfully then 0 else 1.]
        """

        try:
            table_name,_,_ = self.make_dataset_schema() # Get table name,schema and columns from dataset class.

            sql_command = f"SELECT USER_NAME FROM {table_name} WHERE DATASET_ID = '{dataset_id}'"
            user_name_df = DBObject.select_records(connection,sql_command) 
            user_name_from_table = user_name_df['user_name'][0]
            
            if user_name == user_name_from_table:

                #? This condition will be false when called form delete_project_details function,
                #? because that function has already checked that this dataset is used nowhere
                if not skip_check:   
                    ProjectObject = project_creation.ProjectClass() # Get dataset class object

                    project_table_name,_,_ = ProjectObject.make_project_schema()
                    
                    sql_command = f"SELECT PROJECT_ID FROM {project_table_name} WHERE DATASET_ID = '{dataset_id}'"
                    dataset_ids_df = DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
                    id_count = len(dataset_ids_df)
                else:
                    id_count = 0
                    
                if id_count == 0: #? Number of projects that use this dataset
                    
                    #? Getting csv table name
                    sql_command = "SELECT DATASET_TABLE_NAME FROM "+ table_name + " WHERE DATASET_ID ='"+ dataset_id +"'"
                    dataset_df=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
                    dataset_table_name = dataset_df['dataset_table_name'][0] 

                    sql_command = f"DELETE FROM {table_name} WHERE DATASET_ID = '{dataset_id}'"
                    dataset_status = DBObject.delete_records(connection,sql_command)

                    #? Deleting the CSV Table
                    dataset_table_name = dataset_table_name.lower()
                    data_status = self.delete_data_details(DBObject,connection,dataset_table_name,user_name)
                        
                    if dataset_status == 0 and data_status == 0: return 0
                    else: return 1
                else:
                    #? More than 1 project is using this dataset, can't delete it.
                    return 1
            else:
                return 1
        except:
            return 1
        
    #* Version 1.2
    def delete_data_details(self,DBObject,connection,table_name,user_name):
        """
        This function is used to delete the whole table which was created from 
        user input file.
        
        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            table_name ([string]): [Name of the table that you want to delete.]
            user_name ([string]): [Name of the user.]

        Returns:
            [integer]: [it will return status of the dataset deletion. if successfully then 0 else 1.]
        """
        
        #? Creating Sql Query
        sql_command = 'DROP TABLE '+ user_name +'.'+table_name
        status = DBObject.delete_records(connection,sql_command)
        
        return status

    def dataset_exists(self,DBObject,connection,table_name,dataset_visibility,dataset_name,user_name):
        """This function is used to check existing dataset name.

        Args:
            DBObject ([object]): [object of the database class.]
            connection ([object]): [object of the database connection.]
            table_name ([string]): [name of the table.]
            dataset_name ([string]): [name of the dataset.]
            user_name ([string]): [name of the user.]

        Returns:
            [boolean | integer]: [it will return False if no dataset with same name does not exists,
                                    or else it will return the id of the existing dataset]
        """
        
        #? Checking if the same dataset is there for the same user in the dataset table? If yes, then it will not insert a new row in the table
        try:
            #? There can't be 2 public datasets with same name, because that will create ambiguity in Dropdown list
            #? But there can be 2 private datasets with same name, if users are different
            if dataset_visibility == 'public':
                #? Is there any(public & private) dataset with same name?
                sql_command = f"SELECT DATASET_ID FROM {table_name} WHERE DATASET_NAME = '{dataset_name}'"
                #! Possible Security Issue: User will get to know that some other user has private dataset with same name
            else:
                #? Is there any public dataset with same name?
                sql_command = f"SELECT DATASET_ID FROM {table_name} WHERE DATASET_NAME = '{dataset_name}' AND DATASET_VISIBILITY = 'public'"
                data_df=DBObject.select_records(connection,sql_command)
                data=len(data_df)

                if data == 0:
                    #? No public dataset with same name
                    #? Is there any private dataset from you with same name?
                    sql_command = f"SELECT DATASET_ID FROM {table_name} WHERE DATASET_NAME = '{dataset_name}' AND USER_NAME = '{user_name}'"
                else:
                    #! There is a public dataset with your name
                    return int(data_df['dataset_id'][0])
            
            data_df=DBObject.select_records(connection,sql_command)
            data=len(data_df)
            
            if data == 0: return False
            else: return int(data_df['dataset_id'][0])
            #else: return True
        except:
            return False




    



