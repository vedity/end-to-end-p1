import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')
      
class TestIngestPostDataset(unittest.TestCase):
    
    def testscenario1_insert_dataset(self):
        
        #? Changed the path so that the file can be detected in Gitlab CI/CD -Jay
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        #r = requests.post(endpoint, params=args, json=data, files=file)
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        #self.assertEqual(response.json(),{"key":"value"})
        self.assertEqual(status,"200")
    
    def testscenario2_insert_invalid_dataset(self):
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        #r = requests.post(endpoint, params=args, json=data, files=file)
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        #self.assertEqual(response.json(),{"key":"value"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
    

    def testscenario3_insert_invalidfile_dataset(self):
        files ='../unhappyface.png'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"invalid_auto_user","dataset_name":"ivalid_auto_dataset_name","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
       

class TestIngestGetDataset(unittest.TestCase):
    def testscenario4_get_dataset(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data = {"user_name":"autouser"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testscenario5_get__invalidfile_dataset(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data = {"user_name":"invalid_auto_user"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

# class TestIngestDatasetDeletion(unittest.TestCase):
#     def testscenario6_delete_project(self):
#         response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data ={"user_name":"autouser"})
#         response_data = response.json()
#         json_dataset_id = response_data["response"][0]["dataset_id"]
#         response = requests.delete("http://localhost:8000/mlaas/ingest/delete/project_detail/",data ={"user_name":"autouser","dataset_id":json_dataset_id})
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"200")
    
  
class TestIngestPostProject(unittest.TestCase):
    def testscenario7_insert_project(self):
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data = {"user_name":"autouser"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public","dataset_id":json_dataset_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testscenario8_insert_project(self):
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
    
    def testscenario8_insert_project(self):
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

        
    def testscenario9_insert__repeat_project(self):
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")


class TestIngestGetProject(unittest.TestCase):
    def testscenario10_get_project_detail(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",data ={"user_name":"autouser"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testscenario11_get_all_project(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",data ={"user_name":"autouser_invalid"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

        
  
class TestIngestProjectDeletion(unittest.TestCase):
    def testscenario12_delete_project(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",data ={"user_name":"autouser"})
        json_response = response.json()
        project_id = json_response["response"][0]["project_id"]
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/project_detail/",data ={"user_name":"autouser","project_id":project_id})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

