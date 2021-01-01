import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')
      
class TestAIngestPostDataset(unittest.TestCase):
    def testAscenario1_insert_dataset(self):
        '''
        this function will test create_dataset POST method
        take info as data in which arguments are pass to the 
        given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.
        '''
        time.sleep(1)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
    
    def testBscenario2_insert_invalid_dataset(self):
        '''
        this function will test create_dataset POST method with invalid details
        take info as data in which arguments are pass to the 
        given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.
        '''
        time.sleep(1)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
    

    def testCscenario3_insert_invalidfile_dataset(self):
        '''
        this function will test create_dataset POST method with invalid file(non-csv)
        take info as data & file in which arguments are pass to the 
        given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.
        '''
        time.sleep(1)
        files ='../unhappyface.png'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"invalid_auto_user","dataset_name":"ivalid_auto_dataset_name","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
       

class TestBIngestGetDataset(unittest.TestCase):
    def testAscenario4_get_dataset(self):
        '''
        this function will test create_dataset GET method with valid username
        take user_name as arguments and pass to the given URL and it give back 
        the response into a json format.Extract the status_code from 
        response and match with the outcome we prefer.
        '''
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testBscenario5_get__invalidfile_dataset(self):
        '''
        this function will test create_dataset GET method with invalid username
        take user_name as arguments and pass to the given URL and it give back 
        the response into a json format.Extract the status_code from 
        response and match with the outcome we prefer.
        '''
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"invalid_auto_user"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

# # class TestIngestDatasetDeletion(unittest.TestCase):
# #     def testscenario6_delete_project(self):
# #         response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data ={"user_name":"autouser"})
# #         response_data = response.json()
# #         json_dataset_id = response_data["response"][0]["dataset_id"]
# #         response = requests.delete("http://localhost:8000/mlaas/ingest/delete/project_detail/",data ={"user_name":"autouser","dataset_id":json_dataset_id})
# #         json_response = response.json()
# #         status = json_response["status_code"]
# #         self.assertEqual(status,"200")
    
  
class TestCIngestPostProject(unittest.TestCase):
    def testAscenario7_insert_project(self):
        '''
        this function will test create_project POST method
        take info as data in which arguments are pass to the 
        given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.
        '''
        time.sleep(2)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name_project","visibility":"public","dataset_id":json_dataset_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testBscenario8_insert_project(self):
        '''
        this function will test create_project POST method with valid data
        take info as data in which arguments are pass to the 
        given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        time.sleep(2)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
    
    def testCscenario9_insert_project(self):
        '''
        this function will test create_project POST method with invalid data with(visibilty:private)
        take info as data in which arguments are pass to the 
        given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        time.sleep(2)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

        
    def testDscenario10_insert_repeat_project(self):
        '''
        this function will test create_project POST method with invalid data with(visibilty:public)
        take info as data in which arguments are pass to the 
        given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        time.sleep(2)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")


class TestDIngestGetProject(unittest.TestCase):
    
    def testAscenario11_get_project_detail(self):
        '''
        this function will test create_project GET method with valid username and
        pass as argument to the given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_second"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testBscenario12_get_all_project(self):
        '''
        this function will test create_project GET method with invalid username and
        pass as argument to the given URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_invalid"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

        
  
class TestEIngestProjectDeletion(unittest.TestCase):
    def testAscenario13_delete_project(self):
        '''
        this function will test DeleteProject DELETE method.
        first get valid user_name and project_id from the GET method of create_project.
        pass as argument to the Delete method in URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser"})
        json_response = response.json()
        project_id = json_response["response"][0]["project_id"]
        self.assertEqual(project_id,1)
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/project_detail/",params ={"user_name":"autouser","project_id":project_id})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

class TestFIngestDataDetailClass(unittest.TestCase):
    def testAscenario13_datadetail(self):
        '''
        this function will test DataDetail GET method(dataset_visibity=public).
        first get the valid user_name,dataset_table_name and dataset_visibility 
        from the GET method of Create_dataset and pass as argument to the
        GET method of DataDetail URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params ={"user_name":"autouser"})
        json_response = response.json()
        datadetail_username = json_response["response"][0]["user_name"]
        datadetail_tablename = json_response["response"][0]["dataset_table_name"]
        datadetail_visibility = json_response["response"][0]["dataset_visibility"]
        response = requests.get("http://localhost:8000/mlaas/ingest/data_detail/",params ={"user_name":datadetail_username,"table_name":datadetail_tablename,"dataset_visibility":datadetail_visibility})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testBscenario13_datadetail(self):
        '''
        this function will test DataDetail GET method(dataset_visibity=private).
        first POST the valid data into the Dataset Table with private visibilty then,
        get the valid user_name,dataset_table_name and dataset_visibility,and pass as argument to the
        GET method of DataDetail URL and it give back the response into a json format.
        Extract the status_code from response and match with the outcome we prefer.

        '''
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_seconduser","dataset_name":"auto_dataset_name_seconduser","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
    
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params ={"user_name":"autouser_seconduser"})
        json_response = response.json()
        datadetail_username = json_response["response"][0]["user_name"]
        datadetail_tablename = json_response["response"][0]["dataset_table_name"]
        datadetail_visibility = json_response["response"][0]["dataset_visibility"]
        response = requests.get("http://localhost:8000/mlaas/ingest/data_detail/",params ={"user_name":datadetail_username,"table_name":datadetail_tablename,"dataset_visibility":datadetail_visibility})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
