'''
/*CHANGE HISTORY

 --CREATED BY-------------CREATION DATE-------------VERSION-----------PURPOSE----------------------
 Shivani Bhalodiya        18-FEB-2021                 1.0             Initial Version 
 
 */
'''

class ModelFailed(Exception):
    """Model Failed Exception"""
    def __init__(self,status_code):
        self.msg = "Model failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ExperimentDosenotExist(Exception):
    """Dataset Creation Failed Exception"""
    def __init__(self,status_code):
        self.msg = "Dataset creation failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ModelIdDosenotExist(Exception):
    """Dataset Creation Failed Exception"""
    def __init__(self,status_code):
        self.msg = "Dataset creation failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)
