import unittest 
import requests
import json
import time

scenario1 ={

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
    },
    {
            "column_name": "user_name",
            "data_type": "text",
            "column_attribute": "ignore",
            "change_column_name": "user_name"
    },
    {
        "column_name": "password",
        "data_type": "text",
        "column_attribute":"target",
        "change_column_name":"password"
    
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

        

        
# class testBDataSchemaClass(unittest.TestCase):

#     def testA_scenario1_samecolumnanme(self):
        
#         time.sleep(1)
#         info = {"project_id" : 83}
#         response = requests.post("http://localhost:8000/mlaas/ingest/dataset_schema/",params= info,json = scenario1)
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"200")
        