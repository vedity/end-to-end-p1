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
    """Experiment Does not Exist Exception"""
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


class DataDosenotExist(Exception):
    """Data Dose Not Exist Exception"""
    def __init__(self,status_code):
        self.msg = "Dataset creation failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ModelIsStillInQueue(Exception):
    """Model Is Still Is In Queue Exception"""
    def __init__(self,status_code):
        self.msg = "Model Is Still In Queue"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)
        
class ExperimentAlreadyExist(Exception):
    """Experiment Does not Exist Exception"""
    def __init__(self,status_code):
        self.msg = "Experiment Already Exist"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)
