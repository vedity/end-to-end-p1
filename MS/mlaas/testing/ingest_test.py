import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')
class TestAIngestPostDatasetClass(unittest.TestCase):
    def testA_scenario1_insert_dataset(self):
        """This function is used to test the CreateDataset POST Method With valid Data Inputs .

        Args:
            user_name ([string]): [name of the user.]
            dataset_name ([string]): [name of the dataset.],
            visibility ([string]): [name of the visibility(public or private)]
            inputfile([file]): [CSV file]
    
        """
        time.sleep(1)
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
       
        status = json_response["status_code"]
        self.assertEqual(status,"200")

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
        files ='../unhappyface.png'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"invalid_auto_user","dataset_name":"invalid_auto_dataset_name","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

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
        files = '../ingest/dataset/pima_indians_diabetes.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

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
        files = '../ingest/dataset/empty.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name3","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
    
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
        files = '../ingest/dataset/one_column.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name3","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")


    
    
    def testF_scenario6_insert_invalid_dataset(self):
        """This function is used to test the CreateDataset POST Method With invalid Data Inputs .
           Application should not let user upload the CSV files with junk data in Name of Rows and Columns Invalid column name(which contain special characters)
        Args:
            user_name ([string]): [name of the user.]
            dataset_name ([string]): [name of the dataset.],
            visibility ([string]): [name of the visibility(public or private)]
            inputfile([file]): [Special Character Column CSV file] 
    
        """
        time.sleep(1)
        files = '../ingest/dataset/Mall_Customers.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","dataset_name":"auto_dataset_name2","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
    


       

class TestBIngestGetDataset(unittest.TestCase):
    def testA_scenario1_get_dataset(self):
        """ This function is used to test the CreateDataset GET Method With valid Username Input .

        Args:
            user_name ([string]): [name of the user.]
    
        """
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testB_scenario2_get__invalidfile_dataset(self):
        """ This function is used to test the CreateDataset GET Method With invalid Username Input .

        Args:
            user_name ([string]): [name of the user.]
    
        """
        time.sleep(2)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"invalid_auto_user_name"})
        json_response = response.json()
        data = json_response["response"]
        status = "500"
        for x in range(len(data)):
            if data[x]["user_name"] == "invalid_auto_user_name":
                status ="200"
        self.assertEqual(status,"500")

class TestIngestDatasetDeletion(unittest.TestCase):
    def testA_scenario1_delete_dataset(self):
        """ This function is used to test the DeleteDataset DELETE Method With valid user_name .
            Users can delete the dataset uploaded by them.
        Args:
            user_name ([string]): [name of the user.]
            dataset_id ([integer]):[id of the dataset.]
        """
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_valid","dataset_name":"auto_dataset_name_valid","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params ={"user_name":"autouser_valid"})
        response_data = response.json()
        json_dataset_id = response_data["response"][1]["dataset_id"]
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/dataset_detail/",params ={"user_name":"autouser_valid","dataset_id":json_dataset_id})
        json_response = response.json()
        
        status = json_response["status_code"]
        self.assertEqual(status,"200")
    
    def testB_scenario2_delete_dataset(self):
        """ This function is used to test the DeleteDataset DELETE Method With invalid dataset_id(public)  .
            Negative testing Users can delete the dataset uploaded by them Another User cannot delete the public dataset         
        Args:
            user_name ([string]): [name of the user.]
            dataset_id ([integer]):[id of the dataset.]
            
        """
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_four","dataset_name":"auto_dataset_name_four","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser_four"})
        json_response = responsedataset.json()
        dataset_id=json_response["response"][0]["dataset_id"]
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/dataset_detail/",params ={"user_name":"autouser","dataset_id":dataset_id})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

    def testC_scenario3_delete_dataset(self):
        """ This function is used to test the DeleteDataset DELETE Method With invalid dataset(private)  .
            Negative testing : Users can delete the dataset uploaded by them User cannot delete the private dataset of another user.
        Args:
            user_name ([string]): [name of the user.]
            dataset_id ([integer]):[id of the dataset.]

        """
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_five","dataset_name":"auto_dataset_name_five","visibility":"private"}
        response_private_datset = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        responsedataset1 = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser_five"})
        json_response1 = responsedataset1.json()
        dataset_id1=json_response1["response"][0]["dataset_id"]
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_response = responsedataset.json()
        dataset_id=json_response["response"][0]["dataset_id"]
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/dataset_detail/",params ={"user_name":"autouser","dataset_id":dataset_id1})
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
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_six","dataset_name":"autouser_six","visibility":"private"}
        response_private_datset = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser_six"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        info1 = {"user_name":"autouser_six","project_name":"auto_project_six","description":"this is automated entry","dataset_name":"reautouser_six","visibility":"private","dataset_id":json_dataset_id}
        response_project = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info1,files = file)
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/dataset_detail/",params ={"user_name":"auto_project_six","dataset_id":json_dataset_id})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")



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
        info = {"user_name":"autouser_second","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name","visibility":"public"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
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
        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params = {"user_name":"autouser"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name_project","visibility":"public","dataset_id":json_dataset_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")
        

    def testC_scenario3_insert_project(self):
        """ This function is used to test the CreateProject POST Method With invalid dataset_id .
            User is not allowed to use dataset or create project on different user's dataset.       
        Args:
            user_name ([string]): [name of the user.]
            project_name ([string]): [name of the project.],
            description ([string]): [write about project info.],
            dataset_name ([string]): [write about project info.],
            visibility ([string]): [name of the visibility(public)],
            dataset_id ([integer]) :[id of the dataset]
    
        """
        time.sleep(2)
        files = '../ingest/dataset/CarPrice_Assignment.csv'
        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser_three","project_name":"auto_project_name_three","description":"this is automated entry","dataset_name":"auto_dataset_name_project","visibility":"private"}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)

        responsedataset = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params = {"user_name":"autouser_three"})
        json_responsedataset=responsedataset.json()
        json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
        files = '../ingest/dataset/CarPrice_Assignment.csv'

        file = {'inputfile': open(files, 'rb')}
        info = {"user_name":"autouser","project_name":"auto_project_name","description":"this is automated entry","dataset_name":"auto_dataset_name_project","visibility":"public","dataset_id":json_dataset_id}
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")
    
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
        response = requests.post("http://localhost:8000/mlaas/ingest/create_project/",data = info,files = file)
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
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser"})
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
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser_invalid"})
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
        response = requests.get("http://localhost:8000/mlaas/ingest/create_project/",params ={"user_name":"autouser"})
        json_response = response.json()
        project_id = json_response["response"][0]["project_id"]
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/project_detail/",params ={"user_name":"autouser","project_id":project_id})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"200")

    def testB_scenario4_delete_project(self):
        """ This function is used to test the DeleteProject DELETE Method With invalid user name and project id .
            Negative testing:Delete Project When user deletes a project, its dataset will not get deleted
        Args:
            user_name ([string]): [name of the user.]
            project_id ([string]): [id of project table],
            
        """
        time.sleep(2)
        response = requests.delete("http://localhost:8000/mlaas/ingest/delete/project_detail/",params ={"user_name":"invalid_autouser","project_id":2})
        json_response = response.json()
        status = json_response["status_code"]
        self.assertEqual(status,"500")

class TestFIngestDataDetailClass(unittest.TestCase):
    # def testA_scenario1_datadetail(self):
    #     """ This function is used to test the DataDetail GET Method With valid inputs.
    #         Raw data of the dataset uploaded for the project
    #     Args:
    #         dataset_id ([integer]): [Id of the dataset.]
           

    #     """
    #     request_data = {
    #         "draw": 1,
    #         "columns": [{"data": "id","name": "","searchable": "true","orderable": "true",
    #         "search": {"value": "","regex": "false"}},
    #         {
    #         "data": "firstName","name": "","searchable": "true","orderable": "true","search": {
    #         "value": "",
    #         "regex": "false"}},
    #         {"data": "lastName","name": "","searchable": "true","orderable": "true","search": {
    #         "value": "",
    #         "regex": "false"}}], "order": [{"column": 0,"dir": "asc"}],
    #         "start": 1,"length": 10,"search": { "value": "","regex": "false" },"customfilter": [{
    #         "username": "admin",
    #         "uid":1}]}
        
    #     headers = {'content-type': 'application/json'}
    #     data = json.dumps(request_data)
    #     response = requests.get("http://localhost:8000/mlaas/ingest/create_dataset/",params ={"user_name":"autouser_second"})
    #     json_response = response.json()
    #     datadetail_id = json_response["response"][0]["dataset_id"]
    #     response = requests.post("http://localhost:8000/mlaas/ingest/data_detail/",data = data ,params ={"dataset_id":datadetail_id},headers = headers)
    #     json_response = response.json()
    #     print(json_response)
    #     status = json_response["recordsFiltered"]
    #     self.assertEqual(json_response,205)

    def testB_scenario3_datadetail(self):
        """ This function is used to test the DataDetail GET Method With invalid dataset_id.
            Negative testing:raw data of the dataset uploaded for the project.
        Args:
            dataset_id ([integer]): [id of the dataset.]
    
        """
        request_data = {
            "draw": 1,
            "columns": [{"data": "id","name": "","searchable": "true","orderable": "true",
            "search": {"value": "","regex": "false"}},
            {
            "data": "firstName","name": "","searchable": "true","orderable": "true","search": {
            "value": "",
            "regex": "false"}},
            {"data": "lastName","name": "","searchable": "true","orderable": "true","search": {
            "value": "",
            "regex": "false"}}], "order": [{"column": 0,"dir": "asc"}],
            "start": 1,"length": 10,"search": { "value": "","regex": "false" },"customfilter": [{
            "username": "admin",
            "uid":1}]}
        
        headers = {'content-type': 'application/json'}
        data = json.dumps(request_data)
        response = requests.post("http://localhost:8000/mlaas/ingest/data_detail/",data = data ,params ={"dataset_id":0},headers = headers)
        json_response = response.json()
        status = json_response["recordsFiltered"]
        self.assertEqual(status,0)
