import unittest 
import requests
import json
import time

scenario1 ={

   "data" : [{
       "column_name": "index",
        "data_type": "numerical",
        "column_attribute":"target",
        "change_column_name":"index_col "
    },
    {
        "column_name": "uid",
        "data_type": "categorical",
        "column_attribute":"target",
        "change_column_name":"uid_col_changed_2"
    }]
}

scenario2 ={

   "data" : [{
       "column_name": "index",
        "data_type": "numerical",
        "column_attribute":"target",
        "change_column_name":"index"
    },
    {
        "column_name": "uid",
        "data_type": "categorical",
        "column_attribute":"target",
        "change_column_name":"uid"
    }]
}

scenario3 = {
     "data" : [{
       "column_name": "index",
        "data_type": "numerical",
        "column_attribute":"ignore",
        "change_column_name":"index_change"
    },
    {
        "column_name": "uid",
        "data_type": "categorical",
        "column_attribute":"ignore",
        "change_column_name":"uid_change"
    }]
}

class TestADataExplorationClass(unittest.TestCase):
    
    def testA_scenario1_dataset_statisctics(self):
        """ This function is used to test the DatasetStatisticsClass Get Method With dataset_id .

        Args:
            dataset_id ([integer]):[id of the dataset.]
        """
        time.sleep(1)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"}) #get dataset_id
        json_response = responsedataset.json() #get json formate
        dataset_id=json_response["response"][0]["dataset_id"] #fetch dataset id from json
        info = {"dataset_id" : dataset_id} #pass as dictionary in params
        response = requests.get("http://localhost:8000/mlaas/preprocess/exploredata/get_data_statistics",params = info) #send request on base of datasetid
        json_response = response.json() #get json response
        status = json_response["status_code"] #get status code
        self.assertEqual(status,"200") #compare status code
        
class testBDataSchemaClass(unittest.TestCase):

    def testA_scenario1(self):
        """ This function is used to test that application should not allow same name as CSV column name in change column name.
            This is positive test.
        Args:
            project_id ([integer]):[id of the project.]
            Json : [json as scenario1](define in above code)
        """
        time.sleep(1)
        projectid_response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_second"}) #get projectid
        projectid_json_response = projectid_response.json() #projectid in json formate
        project_id = projectid_json_response["response"][0]["project_id"] #fetch projectid from json
        info = {"project_id" : project_id} #request parameter as projectid
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset_schema/",params= info,json = scenario1) #get response
        json_response = response.json() # response to json
        status = json_response["Status"] #fetch response status
        self.assertEqual(status,"200") #compare status

    @unittest.expectedFailure   #this line is for compulsary failure
    def testB_scenario2(self): 
        """ This function is used to test that application should not allow same name as CSV column name in change column name.
            This is negative test.
        Args:
            project_id ([integer]):[id of the project.]
            Json : [json as scenario2](define in above code)
        """      
        time.sleep(1)
        projectid_response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_second"})
        projectid_json_response = projectid_response.json()
        project_id = projectid_json_response["response"][0]["project_id"]
        info = {"project_id" : project_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset_schema/",params= info,json = scenario2)
        json_response = response.json()
        status = json_response["Status"]
        self.assertEqual(status,"200")

    #@unittest.expectedFailure
    def testC_scenario3(self):
        """ This function is used to test that  Application should not allow to choose each column as ignore.
            This is negative test.
        Args:
            project_id ([integer]):[id of the project.]
            Json : [json as scenario3](define in above code)
        """
        time.sleep(1)
        projectid_response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_second"})
        projectid_json_response = projectid_response.json()
        project_id = projectid_json_response["response"][0]["project_id"]
        info = {"project_id" : project_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset_schema/",params= info,json = scenario3)
        json_response = response.json()
        status = json_response["Status"]
        self.assertEqual(status,"200")

    def testD_scenario4(self):
        """ This function is used to test that application should allow to insert multiple column as target column
            This is positive test.
        Args:
            project_id ([integer]):[id of the project.]
            Json : [json as scenario1](define in above code)
        """
        time.sleep(1)
        projectid_response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_second"})
        projectid_json_response = projectid_response.json()
        project_id = projectid_json_response["response"][0]["project_id"]
        info = {"project_id" : project_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset_schema/",params= info,json = scenario1)
        json_response = response.json()
        status = json_response["Status"]
        self.assertEqual(status,"200")

