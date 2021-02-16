import unittest 
import requests
import json
import time
unittest.TestLoader.sortTestMethodsUsing = None
import logging
logger = logging.getLogger('django')



# class TestLogin(unittest.TestCase):
#     def testA_validlogin(self):
#         response = requests.post("http://localhost:8000/mlaas/ingest/common/user/login")
#         info = {"user_name":"nisha","password":"nisha"}
#         response1 = requests.get("http://localhost:8000/mlaas/ingest/common/user/login",params=info)
#         json_response = response1.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"200")

#     def testB_invalidlogin(self):
#         info = {"user_name":"abc","password":"xyz"}
#         response1 = requests.get("http://localhost:8000/mlaas/ingest/common/user/login",params=info)
#         json_response = response1.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"500")

# class ATestIngestDataDeletion(unittest.TestCase):
#     def testA_scenario1_delete_dataset(self):
#         """ This function is used to test the DeleteDataset DELETE Method With valid user_name .
#             Users can delete the dataset uploaded by them.
#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_id ([integer]):[id of the dataset.]
#         """
#         files = '../ingest/dataset/CarPrice_Assignment.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"autouser_valid","dataset_name":"auto_dataset_name_valid","visibility":"private"}
#         response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
#         response = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params ={"user_name":"autouser_valid"})
#         response_data = response.json()
#         json_dataset_id = response_data["response"][0]["dataset_id"]
#         response = requests.delete("http://localhost:8000/mlaas/ingest/dataset/delete/",params ={"user_name":"autouser_valid","dataset_id":json_dataset_id})
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"200")

# class TestAIngestPostDatasetClass(unittest.TestCase):
#     def testA_scenario1_insert_dataset(self):
#         """This function is used to test the CreateDataset POST Method With valid Data Inputs .

#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_name ([string]): [name of the dataset.],
#             visibility ([string]): [name of the visibility(public or private)]
#             inputfile([file]): [CSV file]
    
#         """
        
#         files = '../ingest/dataset/CarPrice_Assignment.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"nisha","dataset_name":"auto_dataset_name","visibility":"public"}
#         response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"200")

    # def testAB_dataset_creationactivity(self):
    #     time.sleep(2)
    #     response = requests.post("http://localhost:8000/mlaas/common/activity/")
    #     info ={"user_name":"autouser"}
    #     response = requests.get("http://localhost:8000/mlaas/common/activity/",params=info)
    #     json_response = response.json()
    #     status = json_response["status_code"]
    #     self.assertEqual(status,"200")      

#     @unittest.expectedFailure
#     def testB_scenario2_insert_invalidfile_dataset(self):
#         """ This function is used to test the CreateDataset POST Method With invalid file Input.
#             Users are only allowed to upload CSV dataset.


#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_name ([string]): [name of the dataset.],
#             visibility ([string]): [name of the visibility(public or private)]
#             inputfile([file]): [PNG file]
    
#         """ 
#         time.sleep(1)
#         files ='../unhappyface.png'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"invalid_auto_user","dataset_name":"invalid_auto_dataset_name","visibility":"private"}
#         response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"200")

#     def testC_scenario1_insert_dataset(self):
#         """This function is used to test the CreateDataset POST Method With duplicate dataset name as Data Inputs .
#            Dataset with duplicate name cannot be created
#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_name ([string]): [name of the dataset.],
#             visibility ([string]): [name of the visibility(public or private)]
#             inputfile([file]): [CSV file] 
    
#         """
#         time.sleep(1)
#         files = '../ingest/dataset/pima_indians_diabetes.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"autouser","dataset_name":"auto_dataset_name","visibility":"public"}
#         response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"500")
        
#     @unittest.expectedFailure
#     def testD_scenario1_insert_dataset(self):
#         """This function is used to test the CreateDataset POST Method With Empty CSV as Invalid Data Inputs .
#            Application should not let user upload the CSV files with junk data in Name of Rows and Columns Empty CSV File(No Data)
#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_name ([string]): [name of the dataset.],
#             visibility ([string]): [name of the visibility(public or private)]
#             inputfile([file]): [Empty CSV file] 
    
#         """
#         time.sleep(1)
#         files = '../ingest/dataset/empty.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"autouser","dataset_name":"auto_dataset_name3","visibility":"public"}
#         response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,200)

#     @unittest.expectedFailure
#     def testE_scenario1_insert_invalid_dataset(self):
#         """This function is used to test the CreateDataset POST Method With Invalid Data Inputs .
#            Application should not let user upload the CSV files with junk data in Name of Rows and
#            Columns(file with one column should not be allowed )CSV File with One column
           
#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_name ([string]): [name of the dataset.],
#             visibility ([string]): [name of the visibility(public or private)]
#             inputfile([file]): [One Column CSV file] 
    
#         """
#         time.sleep(1)
#         files = '../ingest/dataset/one_column.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"autouser","dataset_name":"auto_dataset_name3","visibility":"public"}
#         response = requests.post("http://localhost:8000/mlaas/ingest/create_dataset/",data = info,files = file)
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,200)      

    


# class TestBIngestGetDataset(unittest.TestCase):
#     def testA_scenario1_get_dataset(self):
#         """ This function is used to test the CreateDataset GET Method With valid Username Input .

#         Args:
#             user_name ([string]): [name of the user.]
    
#         """
#         time.sleep(2)
#         response = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser"})
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"200")

#     @unittest.expectedFailure
#     def testB_scenario2_get__invalidfile_dataset(self):
#         """ This function is used to test the CreateDataset GET Method With invalid Username Input .

#         Args:
#             user_name ([string]): [name of the user.]
    
#         """
#         time.sleep(2)
#         response = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"invalid_auto_user_name"})
#         json_response = response.json()
#         data = json_response["response"]
#         status = "500"
#         for x in range(len(data)):
#             if data[x]["user_name"] == "invalid_auto_user_name":
#                 status ="200"
#         self.assertEqual(status,"200")

# class TestIngestDatasetDeletion(unittest.TestCase):


#     def testB_scenario2_delete_dataset(self):
#         """ This function is used to test the DeleteDataset DELETE Method With invalid dataset_id(public)  .
#             Negative testing Users can delete the dataset uploaded by them Another User cannot delete the public dataset         
#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_id ([integer]):[id of the dataset.]
            
#         """
#         files = '../ingest/dataset/CarPrice_Assignment.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"autouser_four","dataset_name":"auto_dataset_name_four","visibility":"private"}
#         response = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
#         responsedataset = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser_four"})
#         json_response = responsedataset.json()
#         dataset_id=json_response["response"][0]["dataset_id"]
#         response = requests.delete("http://localhost:8000/mlaas/ingest/dataset/delete/",params ={"user_name":"abc","dataset_id":dataset_id})
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"500")

    
#     def testD_scenario4_delete_dataset(self):
#         """ This function is used to test the DeleteDataset DELETE Method With invalid dataset(private)  .
#             Datasets which are already being used by projects cannot be deleted.
#         Args:
#             user_name ([string]): [name of the user.]
#             dataset_id ([integer]):[id of the dataset.]

#         """
#         files = '../ingest/dataset/CarPrice_Assignment.csv'
#         file = {'inputfile': open(files, 'rb')}
#         info = {"user_name":"autouser_six","dataset_name":"autouser_six","visibility":"private"}
#         response_private_datset = requests.post("http://localhost:8000/mlaas/ingest/dataset/create/",data = info,files = file)
#         responsedataset = requests.get("http://localhost:8000/mlaas/ingest/dataset/create/",params = {"user_name":"autouser_six"})
#         json_responsedataset=responsedataset.json()
#         json_dataset_id = json_responsedataset["response"][0]["dataset_id"]
#         info1 = {"user_name":"autouser_six","project_name":"auto_project_six","description":"this is automated entry","dataset_name":"reautouser_six","visibility":"private","dataset_id":json_dataset_id}
#         response_project = requests.post("http://localhost:8000/mlaas/ingest/project/create/",data = info1,files = file)
#         response = requests.delete("http://localhost:8000/mlaas/ingest/dataset/delete/",params ={"user_name":"auto_project_six","dataset_id":json_dataset_id})
#         json_response = response.json()
#         status = json_response["status_code"]
#         self.assertEqual(status,"500")



