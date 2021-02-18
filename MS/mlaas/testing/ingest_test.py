import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')

class ATestLogin(unittest.TestCase):
    def testA_validlogin(self):
        response_activity = requests.post("http://localhost:8000/mlaas/common/activity/")
        response = requests.post("http://localhost:8000/mlaas/ingest/common/user/login")
        info = {"user_name":"nisha","password":"nisha"}
        response1 = requests.get("http://localhost:8000/mlaas/ingest/common/user/login",params=info)
        json_response = response1.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testB_invalidlogin(self):
        info = {"user_name":"abc","password":"xyz"}
        response1 = requests.get("http://localhost:8000/mlaas/ingest/common/user/login",params=info)
        json_response = response1.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

# class ATestIngestDataDeletion(unittest.TestCase):
#     def testA_scenario1_delete_dataset(self):
#         """ This function is used to test the DeleteDataset DELETE Method With valid user_name .
#             Users can delete the dataset uploaded by them.
#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_id ([integer]):[id of the dataset.]
#         """
#         files = 'ingest/dataset/CarPrice_Assignment.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"autouser_valid","dataset_name":"auto_dataset_name_valid","visibility":"private","dataset_description":"dataset description"}
#         response1 = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
# class BTestDeletion(unittest.TestCase):        
#     def testB_scenario2_delete_dataset(self):
        
#         response = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params ={"user_name":"autouser_valid"})
#         response_data = response.json()
#         json_dataset_id = response_data["response"][0]["dataset_id"]
#         response2 = requests.delete("http://localhost:8000/mlaas/ingest/dataset/delete/",params ={"user_name":"autouser_valid","dataset_id":json_dataset_id})
#         json_response = response2.json()
#         status = json_response["status_code"]
#         self.assertEqual(json_response,"200")

class TestAIngestPostDatasetClass(unittest.TestCase):
    def testA_scenario1_insert_dataset(self):
        """This function is used to test the CreateDataset POST Method With valid Data Inputs .

        Args:
            user_name ([string]): [name of the user.]
            dataset_name ([string]): [name of the dataset.],
            visibility ([string]): [name of the visibility(public or private)]
            inputfile([file]): [CSV file]
    
        """
        
        
        files = 'ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_user","visibility":"private","dataset_description":"dataset"}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    
    @unittest.expectedFailure
    def testB_scenario2_insert_invalidfile_dataset(self):
        """ This function is used to test the CreateDataset POST Method With invalid file Input.
            Users are only allowed to upload CSV dataset.


        Args:
            user_name ([string]): [name of the user.]
            dataset_name ([string]): [name of the dataset.],
            visibility ([string]): [name of the visibility(public or private)]
            inputfile([file]): [PNG file]
    
        """ 
        time.sleep(1)
        files ='unhappyface.png'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"invalid_auto_user","dataset_name":"invalid_auto_dataset_name","visibility":"private","dataset_description":"dataset description"}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testC_scenario1_insert_dataset(self):
        """This function is used to test the CreateDataset POST Method With duplicate dataset name as Data Inputs .
           Dataset with duplicate name cannot be created
        Args:
            user_name ([string]): [name of the user.]
            dataset_name ([string]): [name of the dataset.],
            visibility ([string]): [name of the visibility(public or private)]
            inputfile([file]): [CSV file] 
    
        """
        time.sleep(1)
        files = 'ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public","dataset_description":"dataset description"}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
        
    @unittest.expectedFailure
    def testD_scenario1_insert_dataset(self):
        """This function is used to test the CreateDataset POST Method With Empty CSV as Invalid Data Inputs .
           Application should not let user upload the CSV files with junk data in Name of Rows and Columns Empty CSV File(No Data)
        Args:
            user_name ([string]): [name of the user.]
            dataset_name ([string]): [name of the dataset.],
            visibility ([string]): [name of the visibility(public or private)]
            inputfile([file]): [Empty CSV file] 
    
        """
        time.sleep(1)
        files = 'ingest/dataset/empty.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name3","visibility":"public","dataset_description":"dataset description"}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,200)

    @unittest.expectedFailure
    def testE_scenario1_insert_invalid_dataset(self):
        """This function is used to test the CreateDataset POST Method With Invalid Data Inputs .
           Application should not let user upload the CSV files with junk data in Name of Rows and
           Columns(file with one column should not be allowed )CSV File with One column
           
        Args:
            user_name ([string]): [name of the user.]
            dataset_name ([string]): [name of the dataset.],
            visibility ([string]): [name of the visibility(public or private)]
            inputfile([file]): [One Column CSV file] 
    
        """
        time.sleep(1)
        files = 'ingest/dataset/one_column.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name3","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,200)      

    


class TestBIngestGetDataset(unittest.TestCase):
    def testA_scenario1_get_dataset(self):
        """ This function is used to test the CreateDataset GET Method With valid Username Input .

        Args:
            user_name ([string]): [name of the user.]
    
        """
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    @unittest.expectedFailure
    def testB_scenario2_get__invalidfile_dataset(self):
        """ This function is used to test the CreateDataset GET Method With invalid Username Input .

        Args:
            user_name ([string]): [name of the user.]
    
        """
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"invalid_auto_user_name"})
        json_response = response.json()
        data = json_response["response"]
        status = "500"
        for x in range(len(data)):
            if data[x]["user_name"] == "invalid_auto_user_name":
                status ="200"
        self.assertEqual(status,"200")

class TestIngestDatasetDeletion(unittest.TestCase):


    def testB_scenario2_delete_dataset(self):
        """ This function is used to test the DeleteDataset DELETE Method With invalid dataset_id(public)  .
            Negative testing Users can delete the dataset uploaded by them Another User cannot delete the public dataset         
        Args:
            user_name ([string]): [name of the user.]
            dataset_id ([integer]):[id of the dataset.]
            
        """
        files = 'ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_four","dataset_name":"auto_dataset_name_four","visibility":"private","dataset_description":"dataset description"}
        response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser_four"})
        json_response = responsedataset.json()
        dataset_id=json_response["response"][0]["dataset_id"]
        response = requests.delete("http://localhost:8000/mlaas/ingest/dataset/delete/",params ={"user_name":"abc","dataset_id":dataset_id})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

    
    def testD_scenario4_delete_dataset(self):
        """ This function is used to test the DeleteDataset DELETE Method With invalid dataset(private)  .
            Datasets which are already being used by projects cannot be deleted.
        Args:
            user_name ([string]): [name of the user.]
            dataset_id ([integer]):[id of the dataset.]

        """
        files = 'ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_six","dataset_name":"autouser_six","visibility":"private","dataset_description":"dataset description"}
        response_private_datset = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser_six"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        info1 = {"user_name":"autouser_six","project_name":"auto_project_six","description":"this is automated entry","dataset_name":"reautouser_six","visibility":"private","dataset_id":json_dataset_id}
        response_project = requests.post("http://localhost:8000/mlaas/ingest/project/create/",data = info1,files = file)
        response = requests.delete("http://localhost:8000/mlaas/ingest/dataset/delete/",params ={"user_name":"auto_project_six","dataset_id":json_dataset_id})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
class testX_activity(unittest.TestCase):    
    def testAB_dataset_creationactivity(self):
        time.sleep(1)
        info ={"user_name":"autouser"}
        response = requests.get("http://localhost:8000/mlaas/common/activity/",params=info)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")      

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
        files = 'ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_2","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_datasetname","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/project/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testAA_project_creationactivity(self):
        time.sleep(2)
        info ={"user_name":"autouser"}
        response = requests.get("http://localhost:8000/mlaas/common/activity/",params=info)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")  



    def testB_scenario2_insert_project(self):
        """ This function is used to test the CreateProject(with assigned dataset) POST Method With valid Input .

        Args:
            user_name ([string]): [name of the user.]
            project_name ([string]): [name of the project.],
            description ([string]): [write about project info.],
            dataset_name ([string]): [write about project info.],
            visibility ([string]): [name of the visibility(public or private)]
    
        """
        time.sleep(2)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        files = 'ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name_project","visibility":"public","dataset_id":json_dataset_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/project/create/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
         
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
        files = 'ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_2","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
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
        
    def testAA_project_deleteactivity(self):
        time.sleep(2)
        response = requests.post("http://localhost:8000/mlaas/common/activity/")
        info ={"user_name":"autouser"}
        response = requests.get("http://localhost:8000/mlaas/common/activity/",params=info)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")      



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


