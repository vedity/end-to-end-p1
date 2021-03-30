from selenium import webdriver  
import time  
#from selenium.webdriver.common.keys import Keys  
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import os
import HTMLTestRunner
import pandas as pd
print("sample test case started")  
#driver = webdriver.Chrome()  
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
driver=webdriver.Firefox()

#maximize the window size  
driver.maximize_window() 



class Test_Script():

    def login(self,user_name,password):

        try:
            self.user_name = user_name
            self.password = password
            #navigate to the url  
            driver.get("localhost:4200/")  #get login page 
            #identify the login page  text box and enter the value 
            driver.find_element_by_id("email").clear() #clear the input
            driver.find_element_by_id("email").send_keys(user_name) #send value for email
            time.sleep(3)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(password) #send value for password 
            time.sleep(3)
            driver.find_element_by_id("btnsubmit").click()
            time.sleep(3) 
        except Exception:
            print(Exception)
        # if __name__ == "__main__":
        #     HTMLTestRunner.main()

    def create_project(self):
        try:
            #creating project 
            driver.get("http://localhost:4200/create")  #get project create page
            driver.find_element_by_name("projectname").clear()
            driver.find_element_by_name("projectname").send_keys("autotest1")
            time.sleep(3) 
            driver.find_element_by_name("description").clear()
            driver.find_element_by_name("description").send_keys("auto discription test")
            time.sleep(3) 
            driver.find_element_by_name("datasetname").clear()
            driver.find_element_by_name("datasetname").send_keys("autodatasetname1")
            time.sleep(3)
            driver.find_element_by_name("datasetdescription").clear()
            driver.find_element_by_name("datasetdescription").send_keys("autodatasetdescricption1")
            time.sleep(3)

 
            # files = '../ingest/dataset/CarPrice_Assignment.csv'
            # file = {'inputfile': open(files, 'rb')}
            driver.find_element_by_name("file").clear() 
            driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\PrayagrajPandya\\MLaaS-Project\\end-to-end-p1\\MS\\mlaas\\CarPrice_Assignment.csv")
            time.sleep(10)
            driver.find_element_by_id("btnsubmit").click()
        
            time.sleep(5) 



            #for Reset Button Test:
            #driver.find_element_by_id("btnreset").click()
        except Exception:
            print(Exception)

    def show_data_details(self):
        try:
            #get Data Detail Page
            driver.find_element_by_id("detailicon").click()

            time.sleep(10)  

            #Schema mapping:
            driver.find_element_by_id("ngb-nav-3").click()
            time.sleep(10)
            #driver.find_element_by_id("selectattr_1").click()
        except Exception:
            print(Exception)

    def schema_mapping(self):
        try:
            excle_file = "C:\\Users\\PrayagrajPandya\\MLaaS-Project\\end-to-end-p1\\MS\\mlaas\\preprocessed_house_price_prediction_regression.csv"
            df_files = pd.read_csv(excle_file)
            unique_col = df_files.shape[1]

            #print(unique_col)
            #for column rename:
            for i in range(1,unique_col+1):
                #print("columnname_"+str(i))
                driver.find_element_by_id("columnname_"+str(i)).clear()
                driver.find_element_by_id("columnname_"+str(i)).send_keys("columnname_"+str(i))
                time.sleep(3)
                pass
            time.sleep(10)
            driver.find_element_by_class_name("btn btn-success").click()
            time.sleep(10)

            #for select target Schema in mapping:
            for i in range(1,unique_col+1,2):
                s = Select(driver.find_element_by_xpath("//select[@id='selectattr_'+str(i)]"))
                s.select_by_visible_text("Target")
                time.sleep(3)
                #print('selectattr_'+str(i))
            time.sleep(10)
            driver.find_element_by_class_name("btn btn-success").click()
            time.sleep(10)       

            #for igoner schema in mapping:
            for i in range(2,unique_col+1,2):
                s = Select(driver.find_element_by_xpath("//select[@id='selectattr_'+str(i)]"))
                s.select_by_visible_text("Ignore")
                time.sleep(3)
                #print('selectattr_'+str(i))
            time.sleep(10)
            driver.find_element_by_class_name("btn btn-success").click()
            time.sleep(10)
           

        except Exception:
            print(Exception)

    def upload_dataset_in_exisiting_project(self):
        try:
            ####upload new dataset and add that dataset in existing project:
            #navigate to the url  
            driver.get("http://localhost:4200/dataset")   #get create dataset url

            driver.find_element_by_id("create").click()
            time.sleep(3) 
            driver.find_element_by_name("datasetname").clear()
            driver.find_element_by_name("datasetname").send_keys("House Price")
            time.sleep(3) 
            driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\PrayagrajPandya\\MLaaS-Project\\end-to-end-p1\\MS\\mlaas\\preprocessed_house_price_prediction_regression.csv")
            time.sleep(3)
            driver.find_elements_by_name("datasetdescription").clear()
            driver.find_element_by_name("datasetdescription").send_keys("House Price Prediction")
            time.sleep(5)
            driver.find_element_by_id("btnsubmit").click()
            time.sleep(6)
        except Exception:
            print(Exception)
        
    def close_browser(self):
        try:

            ##
            driver.get("http://localhost:4200/project")
            #close the browser  
            driver.close()  
            print("sample test case successfully completed") 
        except Exception:
            print(Exception)


TS =  Test_Script()
TS.login("mehul","mehul")
# TS.create_project()
# TS.show_data_details()
# TS.schema_mapping()
# TS.upload_dataset_in_exisiting_project()
TS.close_browser()

#git clone https://gitlab.com/isgtest/end-to-end-p1.git

#git pull origin uAT
