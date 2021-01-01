import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')
      
class TestAIngestPostDataset(unittest.TestCase):
    
    def testAscenario1_insert_dataset(self):
        time.sleep(1)
        #? Changed the path so that the file can be detected in Gitlab CI/CD -Jay
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
    
    def testBscenario2_insert_invalid_dataset(self):
        time.sleep(1)
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
    

    def testCscenario3_insert_invalidfile_dataset(self):
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
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testBscenario5_get__invalidfile_dataset(self):
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
        time.sleep(2)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        # self.assertEqual(json_dataset_id,1)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name_project","visibility":"public","dataset_id":json_dataset_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testBscenario8_insert_project(self):
        time.sleep(2)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
    
    def testCscenario9_insert_project(self):
        time.sleep(2)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

        
    def testDscenario10_insert__repeat_project(self):
        time.sleep(2)
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")


class TestDIngestGetProject(unittest.TestCase):
    def testAscenario11_get_project_detail(self):
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_second"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testBscenario12_get_all_project(self):
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_invalid"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

        
  
class TestEIngestProjectDeletion(unittest.TestCase):
    def testAscenario13_delete_project(self):
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
