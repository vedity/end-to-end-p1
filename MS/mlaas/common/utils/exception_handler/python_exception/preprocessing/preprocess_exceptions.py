"""

/*CHANGE HISTORY

--CREATED BY-------------CREATION DATE-------------VERSION-----------PURPOSE----------------------
 Jay Shukla               17-jan-2021                 1.0             Initial Version 

*/

"""

class StatisticsError(Exception):
    """ Get Statistics Error """
    def __init__(self,status_code):
        self.msg = "Error Ocurred while trying to get the Statistics"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
    def __str__(self):
        return (self.msg)
    
    
class SchemaUpdateFailed(Exception):
    """  updating schema table failed"""
    def __init__(self,status_code):
        self.msg = "Schema update failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)


class IgnoreAttributeClass(Exception):
    """  """
    def __init__(self,status_code):
        self.msg = "All attribute type column are Ignore"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)

class TableCreationFailed(Exception):
    """  Table Creation Failed"""
    def __init__(self,status_code):
        self.msg = "Table creation failed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)

class SameColumnNameFound(Exception):
    """  Value of column name and change column name cannot be same"""
    def __init__(self,status_code):
        self.msg = "Same column name are not allowed"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)


class SchemaDataNotFound(Exception):
    """ Schema Data Not Found Exception """
    def __init__(self,status_code):
        self.msg = "Schema data not found"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class TableDataNotFound(Exception):
    """ Table Data Not Found Exception """
    def __init__(self,status_code):
        self.msg = "Table data not found"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg

    def __str__(self):
        return (self.msg)

class InvalidColumnNames(Exception):
    """ InvalidColumnNames """
    def __init__(self,status_code):
        self.msg = " Column name contains '('  ')'  or '%' "
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)

class OperationOrderingFailed(Exception):
    """  Function that Reorders the operation failed."""
    def __init__(self,status_code):
        self.msg = " Operation Reordering Failed."
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)


class ChangeColumnNameSame(Exception):
    """ Raise exception where Change column name  are been same """
    def __init__(self,status_code):
        self.msg = "Column name already assign to other column"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)

class IgnoreColumns(Exception):
    """ All column attribute cannot be Ignored """
    def __init__(self,status_code):
        self.msg = "All column cannot be Ignored"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)
    
class GetDataDfFailed(Exception):
    """ get_data_df function failed to return a dataframe. """
    def __init__(self,status_code):
        self.msg = "get_data_df function failed."
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)
    
class SavingFailed(Exception):
    """ Master Operator function failed to save the data into postgres. """
    def __init__(self,status_code):
        self.msg = "Saving Failed."
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)

class EcondingFailed(Exception):
    """ Encoding failed """
    def __init__(self,status_code):
        self.msg = "Failed to do one-hot-encoding! column having more then five categorical values"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
     
    def __str__(self):
        return (self.msg)