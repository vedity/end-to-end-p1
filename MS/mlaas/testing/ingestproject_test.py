import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')



class TestCIngestPostProject(unittest.TestCase):
    
    def testA_scenario1_insert_project(self):
        """ This function is used to test the CreateProject POST Method With valid Input .

        Args:
            user_name ([string]): [name of the user.]
            project_name ([string]): [name of the project.],
            description ([string]): [write about project info.],
            dataset_name ([string]): [write about project info.],
            visibility ([string]): [name of the visibility(public)]
    
        """
        time.sleep(2)
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_2","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_datasetname","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/project/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    # def testAA_project_creationactivity(self):
    #     time.sleep(2)
    #     info ={"user_name":"autouser"}
    #     response = requests.get("http://localhost:8000/mlaas/common/activity/",params=info)
    #     json_response = response.json()
    #     status = json_response["status_code"]
    #     self.assertEqual(status,"200")      


    # def testB_scenario2_insert_project(self):
    #     """ This function is used to test the CreateProject(with assigned dataset) POST Method With valid Input .

    #     Args:
    #         user_name ([string]): [name of the user.]
    #         project_name ([string]): [name of the project.],
    #         description ([string]): [write about project info.],
    #         dataset_name ([string]): [write about project info.],
    #         visibility ([string]): [name of the visibility(public or private)]
    
    #     """
    #     time.sleep(2)
    #     responsedataset = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser"})
    #     json_responsedataset=responsedataset.json()
    #     json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
    #     files = 'ingest/dataset/CarPrice_Assignment.csv'
    #     file = {'inputfile': open(files, 'rb')}
    #     info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name_project","visibility":"public","dataset_id":json_dataset_id}
    #     response = requests.post("http://localhost:8000/mlaas/ingest/project/create/",data = info,files = file)
    #     json_response = response.json()
    #     status = json_response["status_code"]
    #     self.assertEqual(json_response,"200")
         
    def testD_scenario4_insert_project(self):
        """ This function is used to test the CreateProject POST Method With invalid Input .
            System should not let user create projects with duplicate name (Same as existing projects)
        Args:
            user_name ([string]): [name of the user.]
            project_name ([string]): [name of the project.],
            description ([string]): [write about project info.],
            dataset_name ([string]): [write about project info.],
            visibility ([string]): [name of the visibility(public)]
    
        """
        time.sleep(2)
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/project/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")


class TestDIngestGetProject(unittest.TestCase):
    
    def testA_scenario1_get_project_detail(self):
        """ This function is used to test the CreateProject GET Method With valid user name .
            User can see all projects which are created by user.
        Args:
            user_name ([string]): [name of the user.]
        """
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_2"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testB_scenario2_get_all_project(self):
        """ This function is used to test the CreateProject GET Method With invalid user name .
            Negative testing:User can see all projects which are created by user 
        Args:
            user_name ([string]): [name of the user.]
        """
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_invalid"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")        
  
class TestEIngestProjectDeletion(unittest.TestCase):
    def testA_scenario3_delete_project(self):
        """ This function is used to test the DeleteProject DELETE Method With valid user name and project id .
            Delete Project When user deletes a project, its dataset will not get deleted
        Args:
            user_name ([string]): [name of the user.]
            project_id ([string]): [id of project table],
            
    
        """
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/project/create/",params ={"user_name":"autouser_2"})
        json_response = response.json()
        project_id = json_response["response"][0]["project_id"]
        response = requests.delete("http://localhost:8000/mlaas/ingest/project/delete/",params ={"user_name":"autouser","project_id":project_id})
        response_datasetid = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params ={"user_name":"autouser"})
        json_response = response_datasetid.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
        
    # def testAA_project_deleteactivity(self):
    #     time.sleep(2)
    #     response = requests.post("http://localhost:8000/mlaas/common/activity/")
    #     info ={"user_name":"autouser"}
    #     response = requests.get("http://localhost:8000/mlaas/common/activity/",params=info)
    #     json_response = response.json()
    #     status = json_response["status_code"]
    #     self.assertEqual(status,"200")      



# class TestFIngestDataDetailClass(unittest.TestCase):
#     def testA_scenario1_datadetail(self):
#         """ This function is used to test the DataDetail GET Method With valid inputs.
#             Raw data of the dataset uploaded for the project
#         Args:
#             dataset_id ([integer]): [Id of the dataset.]
#         """
#         request_data = {
#             {"draw":1,"columns":[{"data":0,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":1,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":2,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":3,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":4,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":5,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":6,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}}],"order":[{"column":1,"dir":"asc"}],"start":0,"length":10,"search":{"value":"a","regex":false},"customfilter":{"index":"","car_id":"2","modulename":"","menuname":"","parent_id":"2","url":"","icon":""}}}
        
#         headers = {'content-type': 'application/json'}
#         data = json.dumps(request_data)
#         response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params ={"user_name":"autouser_five"})
#         json_response = response.json()
#         datadetail_id = json_response["response"][0]["dataset_id"]
#         response = requests.post("http://localhost:8000/mlaas/ingest/data_detail/",data = data ,params ={"dataset_id":datadetail_id},headers = headers)
#         json_response = response.json()
#         print(json_response)
#         status = json_response["recordsFiltered"]
#         self.assertEqual(status,205)

