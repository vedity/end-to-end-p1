from selenium import webdriver  
import time  
import uuid
#from selenium.webdriver.common.keys import Keys  
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import os
import pandas as pd
import unittest
import HtmlTestRunner

cont = True
user_name = []
password = []
UAT = []
DatasetStatus = []
ProjectName = []
ProjectDesc = []
DatasetName = []
DatasetDesc = []
FilePath = []
# OutputPath = ""
# OutputPath = "C:\\Users\\PrayagrajPandya\\Downloads\\MLaaS Datasets\\5APR-Report\\"

def get_parameter(strings):
    
    params = []
    for string in strings.split(","):
        start_point = string.find('"')
        end_point = string.find('"',start_point+1)
        parameter = string[start_point+1:end_point]
        if len(parameter) >= 1: params.append(parameter)
    return params

lines = """
project_name : "name2",
project_desc : "desc2",
"""   
get_parameter(lines)

def get_section(section):
    
    all_params = []
    
    for i,sec in enumerate(section.split("---")):
        if i == 0:     
        else:
            all_params.append(get_parameter(sec))  
    return all_params

get_section(file_string)

'''
user_name = input("Enter User Name :")
password = input("Enter Password :")
UAT = input("Run on UAT Server ? (y/n) :")
if UAT == 'y' or UAT == 'Y':
    UAT = 'y'
else :
    UAT = 'n'
while cont:
    dt_status =input("Keep Dataset Private? (y/n) :")
    if dt_status == 'y' or dt_status == 'Y':
        DatasetStatus.append('y')
    else :
        DatasetStatus.append('n')
    ProjectName.append(input("Enter Project Name :"))
    ProjectDesc.append(input("Enter Project Descricption :"))
    DatasetName.append(input("Enter Dataset Name :"))
    DatasetDesc.append(input("Enter Dataset Description :"))
    FilePath.append(input("Enter Dataset file Path :"))
    cont_status = input("Do you want to continue? (y,n) :")
    if cont_status == 'y' or cont_status == 'Y':
        cont = True
    else:
        cont = False
'''
#"C:\\Users\\PrayagrajPandya\\Downloads\\MLaaS Datasets\\Mall_Customers.csv"
#output = "C:\\Users\\PrayagrajPandya\\Downloads\\MLaaS Datasets\\5APR-Report\\"


print("sample test case started") 

#open browser
driver=webdriver.Firefox()
driver.maximize_window()

    
class Test_Script(unittest.TestCase):

    def testA_login(self):
        '''
        This function is used to check login functionality 
        '''
        
        try:
            
            self.user_name = user_name
            self.password = password
            
            if UAT == "y" :
                driver.get("http://isg.loginto.me:4200/") 
            else :
                driver.get("localhost:4200/")

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
    
          
    def testB_create_project(self):
        '''
        #This function is create project 
        '''
        try:
            #print(len(DatasetStatus))
            for i in range(len(DatasetStatus)):
                
                if UAT == "y" :

                    time.sleep(15)
                    driver.get("http://isg.loginto.me:4200/project")    
                    time.sleep(3)
                    driver.find_element_by_id("create").click()
                    time.sleep(5)
                else : 
                    time.sleep(15)
                    driver.get("localhost:4200/project")
                    time.sleep(3)
                    driver.find_element_by_id("create").click()
                    time.sleep(5)
            
                time.sleep(3)
                driver.find_element_by_name("projectname").clear()
                driver.find_element_by_name("projectname").send_keys(ProjectName[i])
                time.sleep(3) 
                driver.find_element_by_name("description").clear()
                driver.find_element_by_name("description").send_keys(ProjectDesc[i])
                time.sleep(3) 
                driver.find_element_by_name("datasetname").clear()
                driver.find_element_by_name("datasetname").send_keys(DatasetName[i])
                time.sleep(3)
                driver.find_element_by_name("datasetdescription").clear()
                driver.find_element_by_name("datasetdescription").send_keys(DatasetDesc[i])
                time.sleep(3)


                driver.find_element_by_name("file").clear() 
                driver.find_element_by_xpath("//input[@type='file']").send_keys(FilePath[i])
                time.sleep(10)
                
                '''
                if DatasetStatus[i] == "y" :
                    pass
                else :
                    time.sleep(5)
                    driver.find_element_by_id("customCheck1").click()
                    time.sleep(3)
                   
                #driver.find_element_by_id("btnsubmit").click()
                time.sleep(15) 
                '''
                status = driver.find_element_by_id("customCheck1").is_displayed()
                print("is displayed method is :",status)
                status = driver.find_element_by_id("customCheck1").is_enabled()
                print("is enable method is :",status)
                status = driver.find_element_by_id("customCheck1").is_selected()
                print("is selected method is :",status)
                status = driver.find_element_by_id("customCheck1").click()
                print("click event is occure :")
                time.sleep(3)
                status = driver.find_element_by_id("customCheck1").is_selected()
                print("is selected method after click is :"status)
                
            
        except Exception:
            print(Exception)

if __name__ =='__main__' :
    
    #for create HTML report:
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports/"))
    