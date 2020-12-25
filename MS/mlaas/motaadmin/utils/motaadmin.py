import pandas as pd 
from .database import db
from .database.db import *

class MotaAdmin:

    def __init__(self,database,user,password,host,port):
        self.database = database # Database Name
        self.user = user # User Name
        self.password = password # Password
        self.host = host # Host Name
        self.port = port # Port Number

    def get_db_connection(self):
        DBObject = db.DBClass() 
        connection,conection_string = DBObject.database_connection(self.database,self.user,self.password,self.host,self.port) 
        return DBObject,connection,conection_string


    def load_data(self):
        table_name = "kc_house_data"
        file_name = "./ingest/dataset/kc_house_data.csv"    
        DBObject,connection,conection_string = self.get_db_connection()
        file_data_df = DBObject.read_data(file_name)
        status = DBObject.load_csv_into_db(conection_string,table_name,file_data_df)
        return status

    def timeline(self):
        DBObject,connection,conection_string = self.get_db_connection()
        sql_command = "SELECT to_date(date,'YYYYMMDD') date from kc_house_data order by to_date(date,'YYYYMMDD') limit 10"
        timeline_data = DBObject.select_records(connection,sql_command)
        return timeline_data

    def total_sales(self):
        DBObject,connection,conection_string = self.get_db_connection()

        sql_command = "SELECT bedrooms,sum(price) price from kc_house_data group by bedrooms"
        bedrooms_price_data = DBObject.select_records(connection,sql_command)

        sql_command = "SELECT bathrooms,sum(price) price from kc_house_data group by bathrooms"
        bathrooms_price_data = DBObject.select_records(connection,sql_command)

        return bedrooms_price_data,bathrooms_price_data

    def show_data_slide_status(self):

        DBObject,connection,conection_string = self.get_db_connection()
     
        sql_command = "SELECT bedrooms,AVG(sqft_living) as sqft_living FROM kc_house_data GROUP BY bedrooms"
        data_details_df = DBObject.select_records(connection,sql_command)
        return data_details_df

    def show_dataset_details(self):
        DBObject,connection,conection_string = self.get_db_connection()      
        sql_command = "SELECT index,(to_date(date,'YYYYMMDD')) date,price,bedrooms,bathrooms FROM kc_house_data limit 5 "
        dataset_df=DBObject.select_records(connection,sql_command)
        return dataset_df
 
    def show_yearly_details(self):
        DBObject,connection,conection_string = self.get_db_connection()   
        sql_command = "SELECT extract(year from (to_date(date,'YYYYMMDD'))) as year,sum(price) as yearly_income from kc_house_data GROUP BY extract(year from (to_date(date,'YYYYMMDD')))"
        dataset_df=DBObject.select_records(connection,sql_command)
        return dataset_df

    def delete_records(self,index):
        DBObject,connection,conection_string = self.get_db_connection()
        sql_command = "DELETE From kc_house_data where index="+str(index)
        status=DBObject.delete_records(connection,sql_command)  
        return status

    def update_records(self,index,date,price,bedrooms,bathrooms):
        DBObject,connection,conection_string = self.get_db_connection()
        sql_command = "UPDATE  kc_house_data set date= "+str(date)+", price= "+str(price)+", bedrooms= "+str(bedrooms)+", bathrooms= "+str(bathrooms)+" where index="+str(index)
        status=DBObject.update_records(connection,sql_command)
        return status
        # sql_command = "UPDATE From kc_house_data set =  where index="+str(index)


    

 
    
    

# MotaAdminObject = MotaAdmin()