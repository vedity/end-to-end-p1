from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  

print("sample test case started")  
#driver = webdriver.Chrome()  
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
driver=webdriver.Firefox()

#maximize the window size  
driver.maximize_window()

#navigate to the url  
driver.get("localhost:4200/")  
#identify the Google search text box and enter the value 
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("nisha")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("nisha")
driver.find_element_by_id("btnsubmit").click()
time.sleep(3)  
time.sleep(3)

#creating project 
driver.get("http://localhost:4200/create")
driver.find_element_by_name("projectname").clear()
driver.find_element_by_name("projectname").send_keys("autotest")

driver.find_element_by_name("description").clear()
driver.find_element_by_name("description").send_keys("auto discription test")

driver.find_element_by_name("datasetname").clear()
driver.find_element_by_name("datasetname").send_keys("autodatasetname")
time.sleep(3)  
time.sleep(3)

#close the browser  
driver.close()  
print("sample test case successfully completed")  