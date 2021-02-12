from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
import os
print("sample test case started")  
#driver = webdriver.Chrome()  
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
driver=webdriver.Firefox()

#maximize the window size  
driver.maximize_window()

#navigate to the url  
driver.get("localhost:4200/")  #get login page
#identify the login page  text box and enter the value 
driver.find_element_by_id("email").clear() #clear the input
driver.find_element_by_id("email").send_keys("nisha") #send value for email
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("nisha") #send value for password 
driver.find_element_by_id("btnsubmit").click()

time.sleep(3)  #sleep time for page loading
time.sleep(3)

#creating project 
driver.get("http://localhost:4200/create")  #get project create page
driver.find_element_by_name("projectname").clear()
driver.find_element_by_name("projectname").send_keys("autotest1")

driver.find_element_by_name("description").clear()
driver.find_element_by_name("description").send_keys("auto discription test")

driver.find_element_by_name("datasetname").clear()
driver.find_element_by_name("datasetname").send_keys("autodatasetname1")

# files = '../ingest/dataset/CarPrice_Assignment.csv'
# file = {'inputfile': open(files, 'rb')}
driver.find_element_by_name("file").clear() 
driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\nbarad\\Desktop\\selenium_mlaas\\end-to-end-p1\\MS\\mlaas\\CarPrice_Assignment.csv")
driver.find_element_by_id("btnsubmit").click()

time.sleep(3) 

#get Data Detail Page
driver.find_element_by_id("icon1").click()


time.sleep(3)  
time.sleep(3)

#close the browser  
driver.close()  
print("sample test case successfully completed")  