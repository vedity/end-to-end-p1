class InvalidCsvFormat(Exception):
    """ CSV Formate Exception """
    def __init__(self,status_code):
        self.msg = "InvalidCSVFormat"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
    def __str__(self):
        return (self.msg)

class NullValue(Exception):
    """ Null Value Exception """
    def __init__(self,status_code):
        self.msg = "NullValue"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
    def __str__(self):
        return (self.msg)

class ArrayIndexOutOfBound(Exception):
    """ Array Index Out Of Bound Exception """
    def __init__(self,status_code):
        self.msg = "ArrayIndexOutOfBound"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
    def __str__(self):
        return (self.msg)

class ValueError(Exception):
    """ Array Index Out Of Bound Exception """
    def __init__(self,status_code):
        self.msg = "ValueError"

    def __str__(self):
        return (self.msg)

class DatabaseConnectionFailed(Exception):
    """ Database Connection Failed Exception """
    def __init__(self,status_code):
        self.msg = "DatabaseConnectionFailed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DatabaseSchemaAlreadyExist(Exception):
    """ Database Schema Already Exist Exception """
    def __init__(self,status_code):
        self.msg = "DatabaseSchemaAlreadyExist"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DatabaseTableAlreadyExist(Exception):
    """ Database Table Already Exist Exception """
    def __init__(self,status_code):
        self.msg = "DatabaseTableAlreadyExist"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg


    def __str__(self):
       return (self.msg)

class DataInsertionFailed(Exception):
    """ Data Insertion Failed Exception"""
    def __init__(self,status_code):
        self.msg = "DataInsertionFailed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg


    def __str__(self):
        return (self.msg)

class DataNotFound(Exception):
    """ Data Not Found Exception"""
    def __init__(self,status_code):
        self.msg = "DataNotFound"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg


    def __str__(self):
        return (self.msg)
    
class TableNotFound(Exception):
    """ Table Not Found Exception"""
    def __init__(self,status_code):
        self.msg = "TableNotFound"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DataDeletionFailed(Exception):
    """ Data Deletion Failed Exception """
    def __init__(self,status_code):
        self.msg = "DataDeletionFailed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DatasetCreationFailed(Exception):
    """Dataset Creation Failed Exception"""
    def __init__(self,status_code):
        self.msg = "DatasetCreationFailed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ProjectCreationFailed(Exception):
    """ Project Creation Failed Exception """
    def __init__(self,status_code):
        self.msg = "ProjectCreationFailed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class  ProjectDataNotFound(Exception):
    """  Project Data Not Found. """
    def __init__(self,status_code):
        self.msg = " ProjectDataNotFound"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class DatasetDataNotFound(Exception):
    """ Dataset Data Not Found Exception """
    def __init__(self,status_code):
        self.msg = "DatasetDataNotFound"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class ProjectAlreadyExist(Exception):
    """ Project Already Exist Exception"""
    def __init__(self,status_code):
        self.msg = "ProjectAlreadyExist"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
       return (self.msg)

class DatasetAlreadyExist(Exception):
    """ Dataset Already Exist Exception"""
    def __init__(self,status_code):
        self.msg = "DatasetAlreadyExist"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class  TooBigFileSize(Exception):
    """  Too Big File Size Exception"""
    def __init__(self,status_code):
        self.msg = "TooBigFileSize"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class  FileNotFound(Exception):
    """  File Not Found Exception"""
    def __init__(self,status_code):
        self.msg = "FileNotFound"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

		
class LoadCSVDataFailed(Exception):
    """  Load CSV Data Failed"""
    def __init__(self,status_code):
        self.msg = "LoadCSVDataFailed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)
