import unittest 
import requests
import json
import time



class TestADataExplorationClass(unittest.TestCase):

    def testA_scenario1_dataset_statisctics(self):

        time.sleep(1)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_response = responsedataset.json()
        dataset_id=json_response["response"][0]["dataset_id"]
        info = {"dataset_id" : dataset_id}
        response = requests.get("http://localhost:8000/mlaas/preprocess/exploredata/get_data_statistics",params = info)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")


        
