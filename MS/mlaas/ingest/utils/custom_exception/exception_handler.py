class InvalidCsvFormat(Exception):
    """ CSV Formate Exception """
    def __init__(self):
        self.msg = "InvalidCSVFormat"
        
    def __str__(self):
        return (self.msg)

class NullValue(Exception):
    """ Null Value Exception """
    def __init__(self):
        self.msg = "NullValue"

    def __str__(self):
        return (self.msg)

class ArrayIndexOutOfBound(Exception):
    """ Array Index Out Of Bound Exception """
    def __init__(self):
        self.msg = "ArrayIndexOutOfBound"

    def __str__(self):
        return (self.msg)

class ValueError(Exception):
    """ Array Index Out Of Bound Exception """
    def __init__(self):
        self.msg = "ValueError"

    def __str__(self):
        return (self.msg)

class DatabaseConnectionFailed(Exception):
    """ Database Connection Failed Exception """
    def __init__(self):
        self.msg = "DatabaseConnectionFailed"

    def __str__(self):
        return (self.msg)

class DatabaseSchemaAlreadyExist(Exception):
    """ Database Schema Already Exist Exception """
    def __init__(self):
        self.msg = "DatabaseSchemaAlreadyExist"

    def __str__(self):
        return (self.msg)

class DatabaseTableAlreadyExist(Exception):
    """ Database Table Already Exist Exception """
    def __init__(self):
        self.msg = "DatabaseTableAlreadyExist"

    def __str__(self):
       return (self.msg)

class DataInsertionFailed(Exception):
    """ Data Insertion Failed Exception"""
    def __init__(self):
        self.msg = "DataInsertionFailed"

    def __str__(self):
        return (self.msg)

class DataNotFound(Exception):
    """ Data Not Found Exception"""
    def __init__(self):
        self.msg = "DataNotFound"

    def __str__(self):
        return (self.msg)
    
class TableNotFound(Exception):
    """ Table Not Found Exception"""
    def __init__(self):
        self.msg = "TableNotFound"

    def __str__(self):
        return (self.msg)

class DataDeletionFailed(Exception):
    """ Data Deletion Failed Exception """
    def __init__(self):
        self.msg = "DataDeletionFailed"

    def __str__(self):
        return (self.msg)

class DatasetCreationFailed(Exception):
    """Dataset Creation Failed Exception"""
    def __init__(self):
        self.msg = "DatasetCreationFailed"

    def __str__(self):
        return (self.msg)

class ProjectCreationFailed(Exception):
    """ Project Creation Failed Exception """
    def __init__(self):
        self.msg = "ProjectCreationFailed"

    def __str__(self):
        return (self.msg)

class  ProjectDataNotFound(Exception):
    """  Project Data Not Found. """
    def __init__(self):
        self.msg = " ProjectDataNotFound"

    def __str__(self):
        return (self.msg)

class DatasetDataNotFound(Exception):
    """ Dataset Data Not Found Exception """
    def __init__(self):
        self.msg = "DatasetDataNotFound"

    def __str__(self):
        return (self.msg)

class ProjectAlreadyExist(Exception):
    """ Project Already Exist Exception"""
    def __init__(self):
        self.msg = "ProjectAlreadyExist"

    def __str__(self):
       return (self.msg)

class DatasetAlreadyExist(Exception):
    """ Dataset Already Exist Exception"""
    def __init__(self):
        self.msg = "DatasetAlreadyExist"

    def __str__(self):
        return (self.msg)

class  TooBigFileSize(Exception):
    """  Too Big File Size Exception"""
    def __init__(self):
        self.msg = "TooBigFileSize"

    def __str__(self):
        return (self.msg)

class  FileNotFound(Exception):
    """  File Not Found Exception"""
    def __init__(self):
        self.msg = "FileNotFound"

    def __str__(self):
        return (self.msg)

		
class LoadCSVDataFailed(Exception):
    """  Load CSV Data Failed"""
    def __init__(self):
        self.msg = "LoadCSVDataFailed"
     
    def __str__(self):
        return (self.msg)

