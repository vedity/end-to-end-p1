import unittest 
import requests
import json
import time

scenario1 ={

   "data" : [{
       "index":29,
       "column_name": "index",
       "data_type": "numerical",
       "column_attribute":"target",
       "change_column_name":"index_col "
    },
    {
        "index":29,
        "column_name": "uid",
        "data_type": "categorical",
        "column_attribute":"target",
        "change_column_name":"uid_col_changed_2"
    }]
}

scenario2 ={

   "data" : [{
       "index":29,
       "column_name": "index",
        "data_type": "numerical",
        "column_attribute":"target",
        "change_column_name":"index"
    },
    {
        "index":29,
        "column_name": "uid",
        "data_type": "categorical",
        "column_attribute":"target",
        "change_column_name":"uid"
    }]
}

scenario3 = {
     "data" : [{
        "index":29,
       "column_name": "index",
        "data_type": "numerical",
        "column_attribute":"ignore",
        "change_column_name":"index_change"
    },
    {
        "index":29,
        "column_name": "uid",
        "data_type": "categorical",
        "column_attribute":"ignore",
        "change_column_name":"uid_change"
    }]
}

scenario4 = {
     "data" : [{
       "index":29,
       "column_name": "index",
        "data_type": "numerical",
        "column_attribute":"",
        "change_column_name":"index_change"
    },
    {
        "index":29,
        "column_name": "uid",
        "data_type": "categorical",
        "column_attribute":"",
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
        responseproject = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params = {"user_name":"autouser"}) #get project_id
        json_response = responseproject.json() #get json formate
        dataset_id=json_response["response"][0]["dataset_id"] #fetch dataset id from json
        schema_id=json_response["response"][0]["schema_id"]
        info = {"dataset_id" : dataset_id,"schema_id":schema_id} #pass as dictionary in params
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
        project_response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_2"}) #get projectid
        projectjson_response = project_response.json() #projectid in json formate
        project_id = projectjson_response["response"][0]["project_id"] #fetch projectid from json
        dataset_id = projectjson_response["response"][0]["dataset_id"] #fetch dataset_id from json
        schema_id = projectjson_response["response"][0]["schema_id"] #fetch schemaid from json
        info = {"project_id" : project_id,"dataset_id":dataset_id,"schema_id":schema_id} #request parameter as projectid
        response = requests.post("http://localhost:8000/mlaas/ingest/preprocess/schema/save/",params= info,json = scenario1) #get response
        json_response = response.json() # response to json
        status = json_response["status_code"] #fetch response status
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
        project_response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_2"}) #get projectid
        projectjson_response = project_response.json() #projectid in json formate
        project_id = projectjson_response["response"][0]["project_id"] #fetch projectid from json
        dataset_id = projectjson_response["response"][0]["dataset_id"] #fetch dataset_id from json
        schema_id = projectjson_response["response"][0]["schema_id"] #fetch schemaid from json
        info = {"project_id" : project_id,"dataset_id":dataset_id,"schema_id":schema_id} #request parameter as projectid
        response = requests.post("http://localhost:8000/mlaas/ingest/preprocess/schema/save/",params= info,json = scenario2)
        json_response = response.json()
        status = json_response["Status"]
        self.assertEqual(status,"200")

    # @unittest.expectedFailure
    # def testC_scenario3(self):
    #     """ This function is used to test that  Application should not allow to choose each column as ignore.
    #         This is negative test.
    #     Args:
    #         project_id ([integer]):[id of the project.]
    #         Json : [json as scenario3](define in above code)
    #     """
    #     time.sleep(1)
    #     project_response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_2"}) #get projectid
    #     projectjson_response = project_response.json() #projectid in json formate
    #     project_id = projectjson_response["response"][0]["project_id"] #fetch projectid from json
    #     dataset_id = projectjson_response["response"][0]["dataset_id"] #fetch dataset_id from json
    #     schema_id = projectjson_response["response"][0]["schema_id"] #fetch schemaid from json
    #     info = {"project_id" : project_id,"dataset_id":dataset_id,"schema_id":schema_id} #request parameter as projectid
    #     response = requests.post("http://localhost:8000/mlaas/ingest/preprocess/schema/save/",params= info,json = scenario3)
    #     json_response = response.json()
    #     status = json_response["status_code"]
    #     self.assertEqual(status,"200")

    def testD_scenario4(self):
        """ This function is used to test that application should allow to insert multiple column as target column
            This is positive test.
        Args:
            project_id ([integer]):[id of the project.]
            Json : [json as scenario1](define in above code)
        """
        time.sleep(1)
        project_response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_2"}) #get projectid
        projectjson_response = project_response.json() #projectid in json formate
        project_id = projectjson_response["response"][0]["project_id"] #fetch projectid from json
        dataset_id = projectjson_response["response"][0]["dataset_id"] #fetch dataset_id from json
        schema_id = projectjson_response["response"][0]["schema_id"] #fetch schemaid from json
        info = {"project_id" : project_id,"dataset_id":dataset_id,"schema_id":schema_id} #request parameter as projectid
        response = requests.post("http://localhost:8000/mlaas/ingest/preprocess/schema/save/",params= info,json = scenario1)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testE_scenario5(self):
        """ This function is used to test that application should allow not to select the Target column.
            This is positive test.
        Args:
            project_id ([integer]):[id of the project.]
            Json : [json as scenario1](define in above code)
        """

        time.sleep(1)
        project_response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_2"}) #get projectid
        projectjson_response = project_response.json() #projectid in json formate
        project_id = projectjson_response["response"][0]["project_id"] #fetch projectid from json
        dataset_id = projectjson_response["response"][0]["dataset_id"] #fetch dataset_id from json
        schema_id = projectjson_response["response"][0]["schema_id"] #fetch schemaid from json
        info = {"project_id" : project_id,"dataset_id":dataset_id,"schema_id":schema_id} #request parameter as projectid
        response = requests.post("http://localhost:8000/mlaas/ingest/preprocess/schema/save/",params= info,json = scenario4)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
