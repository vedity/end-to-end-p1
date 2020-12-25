'''
/*CHANGE HISTORY
--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati          07-DEC-2020           1.0           Initial Version 
 Vipul Prajapati          08-DEC-2020           1.1           Modification for Business Rule ****************************************************************************************/
 
*/
'''
import pandas as pd 
from .database import db

class SchemaClass:
    
    def __init__(self,database,user,password,host,port):
        """This constructor is used to initialize database credentials.
           It will initialize when object of this class is created with below parameter.
           
        Args:
            database ([string]): [name of the database.]
            user ([string]): [user of the database.]
            password ([string]): [password of the database.]
            host ([string]): [host ip or name where database is running.]
            port ([string]): [port number in which database is running.]
        """
        self.database = database # Database Name
        self.user = user # User Name
        self.password = password # Password
        self.host = host # Host Name
        self.port = port # Port Number
    
    def get_dataset_schema(self,dataset_id):
        DBObject = db.DBClass()
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
        
        return None
    
    def map_dataset_schema(self,column_lst,data_type_lst,column_attribute_lst,dataset_id):
        
        return None
    
    def update_dataset_schema(self,dataset_id,user_name):
        DBObject = db.DBClass()
        connection,connection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port)
        schema_status = DBObject.create_schema(connection,user_name)
        
        return None