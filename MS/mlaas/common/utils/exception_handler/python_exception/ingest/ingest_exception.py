'''
/*CHANGE HISTORY

 --CREATED BY-------------CREATION DATE-------------VERSION-----------PURPOSE----------------------
 Shivani Bhalodiya        04-jan-2021                 1.0             Initial Version 
 
 */
'''
class DatasetCreationFailed(Exception):
    """Dataset Creation Failed Exception"""
    def __init__(self,status_code):
        self.msg = "Dataset Creation Failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DatasetDeletionFailed(Exception):
    """Dataset Deletion Failed Exception"""
    def __init__(self,status_code):
        self.msg = "Dataset Deletion Failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class UserAuthenticationFailed(Exception):
    """User Authentication Failed Exception"""
    def __init__(self,status_code):
        self.msg = "User Authentication Failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ProjectDeletionFailed(Exception):
    """Project Deletion Failed Exception"""
    def __init__(self,status_code):
        self.msg = "Project Deletion Failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DatasetInUse(Exception):
    """Dataset InUse Failed Exception"""
    def __init__(self,status_code):
        self.msg = "Dataset  is already IN USE"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ProjectCreationFailed(Exception):
    """ Project Creation Failed Exception """
    def __init__(self,status_code):
        self.msg = "ProjectCreation Failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class  ProjectDataNotFound(Exception):
    """  Project Data Not Found. """
    def __init__(self,status_code):
        self.msg = " ProjectData Not Found"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DatasetDataNotFound(Exception):
    """ Dataset Data Not Found Exception """
    def __init__(self,status_code):
        self.msg = "Dataset Data NotFound"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ProjectAlreadyExist(Exception):
    """ Project Already Exist Exception"""
    def __init__(self,status_code):
        self.msg = "Project Already Exist"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
       return (self.msg)

class DatasetAlreadyExist(Exception):
    """ Dataset Already Exist Exception"""
    def __init__(self,status_code):
        self.msg = "Dataset Already Exist"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

		
class LoadCSVDataFailed(Exception):
    """  Load CSV Data Failed"""
    def __init__(self,status_code):
        self.msg = "Load CSV Data Failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)

