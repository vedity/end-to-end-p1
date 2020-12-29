import unittest 
import requests
import json
unittest.TestLoader.sortTestMethodsUsing = None

      
class TestAPostDataset(unittest.TestCase):
    
    def testA_insert_dataset(self):
        
        #? Changed the path so that the file can be detected in Gitlab CI/CD -Jay
        files = './ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        #r = requests.post(endpoint, params=args, json=data, files=file)
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        #self.assertEqual(response.json(),{"key":"value"})
        self.assertEqual(response.status_code, 200)
    
    def testA_insert_repeat_dataset(self):
        files = './ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        #r = requests.post(endpoint, params=args, json=data, files=file)
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        #self.assertEqual(response.json(),{"key":"value"})
        self.assertEqual(response.status_code, 200)
    
    
    
    
    """ def testA_insert_invalidfile_dataset(self):
        files = b'./unhappyface.png'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"invalid_auto_user","dataset_name":"ivalid_auto_dataset_name","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        self.assertEqual(response.status_code, 200)
     """    

class TestBGetDataset(unittest.TestCase):
    def testB_get_dataset(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data = {"user_name":"autouser","dataset_name":"auto_dataset_name"})
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()), 1)
        json_response=response.json()
        self.assertEqual(len(json_response), 1)

    """ def testB_get__invalidfile_dataset(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data = {"user_name":"invalid_auto_user","dataset_name":"invalid_auto_dataset_name"})
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()), 1)
        json_response=response.json()
        self.assertEqual(len(json_response["Data"]), 0)
 """
  
class TestCPostProject(unittest.TestCase):
    def testC_insert_project(self):
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",data = {"user_name":"autouser"})
        json_responsedataset=responsedataset.json()
        #json_databaseid =json_responsedataset["Data"][0]["dataset_id"]["values"]
        
        #self.assertEqual(json_responsedataset,1)
        files = './ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        self.assertEqual(response.status_code, 200)
        
    def testC_insert__repeat_project(self):
        files = './ingest/dataset/pima_indians_diabetes.csv'
        #files = 'mlaas\pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        self.assertEqual(response.status_code, 200)


class TestDGetProject(unittest.TestCase):
    def testD_get_project_detail(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/project_detail/",data ={"user_name":"autouser"})
        self.assertEqual(response.status_code,200)
        json_response=response.json()
        self.assertTrue(response)
        #self.assertEqual(len(json_response["Data"]), 1)

        
class TestEAllProject(unittest.TestCase):
    def testE_get_all_project(self):
        response = requests.get("http://localhost:8000/mlaas/ingest/project_detail/",data ={"user_name":"autouser"})
        self.assertEqual(response.status_code,200)
        json_response=response.json()
        self.assertTrue(response)
        #self.assertNotEqual(len(json_response["Data"]), 0)
        
    
