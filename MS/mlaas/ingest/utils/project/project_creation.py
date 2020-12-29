'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule
 Jay Shukla               14-DEC-2020           1.3           Added Atomicity in the case where dataset_tbl creation fails.
 Abishek Negi             18-Dec-2020           1.4           need to Check the code not working fine
 Abishek Negi             18-Dec-2020           1.4           Added dataset_id into the arguments 

*/
'''
import pandas as pd
from ..dataset import dataset_creation 
from ..database import db
class ProjectClass:

    def make_project_schema(self):
        """This function is used to make schema for creating project table.
           E.g. column_name  data_type.

        Returns:
            [string]: [it will return name of the table, structure of the table and columns of the table.]
        """
        # Project table name
        table_name = 'mlaas.project_tbl'
        # Columns for project table
        cols = 'project_name,project_desc,user_name,dataset_id' 
        # Schema for project table.
        schema ="project_id bigserial,"\
                "project_name  text,"\
                "project_desc  text,"\
                "dataset_status integer NOT NULL DEFAULT 1,"\
                "model_status integer NOT NULL DEFAULT 1,"\
                "deployment_status integer NOT NULL DEFAULT 1,"\
                "user_name  text,"\
                "dataset_id  bigint,"\
                "created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()" 
                
        return table_name,schema,cols

    def  make_project_records(self,project_name,project_desc,user_name,dataset_id):
        """This function is used to make records for inserting data into project table.
           E.g. column_name_1,column_name_2 .......,column_name_n.

        Args:
            project_name ([string]): [name of the project.],
            project_desc ([string]): [descriptions of the project.],
            user_name ([string]): [name of the user.],
            dataset_id ([integer]): [dataset id of the created dataset.]

        Returns:
            [tuple]: [it will return records in the form of tuple.]
        """
        row = project_name,project_desc,user_name,dataset_id
        row_tuples = [tuple(row)] # Make record for project table.
        return row_tuples
        

    def make_project(self,DBObject,connection,project_name,project_desc,dataset_name,dataset_visibility,file_name ,dataset_id,user_name):
        """This function is used to make project and it will create main project table and also
           load project details into database main project table.
           E.g. project name : sales forecast, travel time prediction etc.
           E.g. project details : project_name,project_desc,file_name,user_name,dataset_table_name.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            project_name ([string]): [name of the project.],
            project_desc ([string]): [descriptions of the project.],
            dataset_name ([string]): [name of the dataset.],
            dataset_visibility ([string]): [visibility of the dataset.],
            file_name ([string]): [name of the file.],
            dataset_id ([integer]): [dataset id of the selected dataset.],
            user_name ([string]): [name of the user.]

        Returns:
            [string,integer]: [it will return status of the project creation and 
            also return project id of the created project.]
        """
        schema_status = DBObject.create_schema(connection)
        # Get table name,schema and columns from dataset class.
        table_name,schema,cols = self.make_project_schema() 
        if self.project_exists(DBObject,connection,table_name,project_name,user_name) : return 2,1
        
        # Get status about create table. if successful then 0 else 1.
        create_status = DBObject.create_table(connection,table_name,schema)
         
        DatasetObject = dataset_creation.DatasetClass()

        if dataset_id == None:
            _,dataset_id = DatasetObject.make_dataset(DBObject,connection,dataset_name,file_name,dataset_visibility,user_name)
        else:
            dataset_id = dataset_id
        
        # Get row for project table.
        row_tuples = self.make_project_records(project_name,project_desc,user_name,dataset_id) 
        # Get status about inserting records into project table. if successful then 0 else 1. 
        insert_status = DBObject.insert_records(connection,table_name,row_tuples,cols) 
        # This condition is used to check project table and data is successfully stored into project table or not.if successful then 0 else 1. 
        if schema_status in [0,1] and create_status in [0,1] and insert_status == 0 :
            status = 0 # Successfully Created
            project_id = self.get_project_id(DBObject,connection,row_tuples,user_name)
        else :
            status = 1 # Failed
            project_id = None

        return status,project_id

    def get_project_id(self,DBObject,connection,row_tuples,user_name):
        """This function is used to get project id of created project.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            row_tuples ([list]): [list of tuple of record.],
            user_name ([string]): [name of the user.]

        Returns:
            [integer]: [it will return the project id of the created project.]
        """
        
        table_name,*_ = self.make_project_schema()
        project_name,*_ = row_tuples[0]
        sql_command = "SELECT project_id from "+ table_name + " Where project_name ='"+ project_name + "' and user_name = '"+ user_name + "'"
        project_df = DBObject.select_records(connection,sql_command)
        project_id = int(project_df['project_id'][0])
        return project_id
    
    def update_dataset_status(self,DBObject,connection,project_id,load_data_status = 0):
        """This function is used to update dataset status field in project table.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            project_id ([integer]): [project id for update dataset status field in project.],
            load_data_status ([integer]): [description]

        Returns:
            [integer]: [it will return stauts of update dataset. if successfully then 1 else 0.]
        """
        table_name,*_ = self.make_project_schema()
        sql_command = "UPDATE "+ table_name + " SET dataset_status=" + str(load_data_status) + " WHERE project_id="+ str(project_id)        
        stauts = DBObject.update_records(connection,sql_command)
        return stauts
    
    def show_project_details(self,DBObject,connection,user_name):
        """This function is used to show details about all created projects.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataframe of the project details.]
        """

        table_name,*_ = self.make_project_schema() # Get table name,schema and columns from dataset class
        # This command is used to get project details from project table of database.
        sql_command = "SELECT * FROM "+ table_name + " WHERE USER_NAME ='"+ user_name +"'"
        project_df=DBObject.select_records(connection,sql_command) # Get project details in the form of dataframe.
        return project_df

    #* Version 1.3
    def delete_project_details(self,DBObject,connection,project_id,user_name):
        """
        This function is used to delete the project entry from the project table.
        It also deletes the dataset if no other project is using it.
        
        Args: 
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            project_id ([number]): [id of the project_tbl entry that you want to delete.],
            user_name ([string]): [name of the user.]

        Returns:
            status ([boolean]): [status of the project deletion. if successfully then 0 else 1.]
        """
        
        try:
            table_name,_,_ = self.make_project_schema()

            #? Fetching original user from the table
            sql_command = f"SELECT USER_NAME FROM {table_name} WHERE PROJECT_ID = '{project_id}'"
            user_name_df = DBObject.select_records(connection,sql_command) 
            user_name_from_table = user_name_df['user_name'][0]
            
            #? Authenticating the user    
            if user_name == user_name_from_table:

                #? Deleting Project Table Entry
                sql_command = "DELETE FROM "+ table_name + " WHERE PROJECT_ID ='"+ project_id +"'"
                project_status = DBObject.delete_records(connection,sql_command)
                
            else:
                project_status = 1
                
            return project_status
        
        except:
            return 1
        
    def show_dataset_names(self,DBObject,connection,user_name):
        """Show all the existing datasets created by user.

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            user_name ([string]): [name of the user.]

        Returns:
            [dataframe]: [it will return dataframe of the selected columns from dataset details.]
        """
        
        DatasetObject = dataset_creation.DatasetClass() # Get dataset class object
        table_name,_,_ = DatasetObject.make_dataset_schema() # Get table name,schema and columns from dataset class.
        # This command is used to get dataset id and names from dataset table of database.
        sql_command = "SELECT dataset_id,dataset_name FROM "+ table_name + " WHERE USER_NAME ='"+ user_name +"' or dataset_visibility='public'"
        dataset_df=DBObject.select_records(connection,sql_command) # Get dataset details in the form of dataframe.
        
        return dataset_df

    #? Check if project with same name 
    def project_exists(self,DBObject,connection,table_name,project_name,user_name):
        """This function is used to check if same name project exist or not .

        Args:
            DBObject ([object]): [object of database class.],
            connection ([object]): [connection object of database class.],
            table_name ([string]): [name of the table.],
            project_name ([string]): [name of the project.],
            user_name ([string]): [name of the user.]

        Returns:
            [boolean]: [it will return true or false. if exists true else false.]
        """
        try:
            #? Checking if Same project_name exists for the same user
            sql_command = f"SELECT PROJECT_ID FROM {table_name} WHERE PROJECT_NAME = '{project_name}' AND USER_NAME = '{user_name}'"
            data=DBObject.select_records(connection,sql_command)
            data=len(data)
            #! Same project_name exists for the same user, then return status True
            if data == 0: return False
            else: return True
        except:
            return False
        
        