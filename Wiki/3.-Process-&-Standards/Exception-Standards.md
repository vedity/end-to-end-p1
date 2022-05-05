###   **Exception** :

An exception is a Python object that represents an error. Python provides a way to handle the exception so that the code can be executed without any interruption. If we do not handle the exception, the interpreter doesn't execute all the code that exists after the exception.

###   **Custom Exception** :

Python has numerous built-in exceptions that force your program to output an error when something in the program goes wrong.

However, sometimes you may need to create your own custom exceptions that serve your purpose.

###  **Example** :

```bash
class NullValue(Exception):
    """ Null Value Exception """
    def __init__(self,status_code):
        self.msg = "Null Value Error"
        self.status_code = status_code
        self.msg = "status_code:" + str(status_code) + ",error_msg:"+self.msg
    def __str__(self):
        return (self.msg)

try:
    a=int(input("Enter number of elements : "));
    if a=0:
       raise Nullvalue(500)
except(NullValue) as exc:
    print(exc.msg)



```

Above defined exception can be raised when database connection could fail.

Refer below mentioned **CUSTOM EXCEPTION** 

| Exception Class | Description |
| ------ | ------ |
| InvalidCsvFormat |Raised when CSV format is Invalid |
| NullValue | Raises when variable has null value|
| DatabaseConnectionFailed | Raised when Database connection is failed |
| DatabaseSchemaAlreadyExist | Raised when Database Schema is already exist in database |
| DatabaseTableAlreadyExist | Raised when Database Table is already exist in database |
| DataInsertionFailed |Raised When Data Insertion in database is failed.|
| DataNotFound | Raised when particular Data can not be found |
| TableNotFound | Raised when we unable to find particular table in database|
| ArrayIndexOutOfBound |Whenever we use an –ve value or, the value greater than or equal to the size of the array, then the ArrayIndexOutOfBoundsException is raised.|
| ValueError | Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified |
| DatasetCreationFailed | Raised when Dataset creation failed |
| ProjectCreationFailed | Raised when Project with same name is already exist |
| ProjectDataNotFound | Raised when Project Data cannot be found |
| DatasetDataNotFound | Raised when Dataset Data cannot be found |
| ProjectAlreadyExist | Raised when Project already exist in database|
| DatasetAlreadyExist | Raised when Dataset already exist in database|
| FileNotFound | Raised when File not found in database|
| LoadCSVDataFailed | Raised when CSV data could not be load|
| GetColumnNamesFailed | Raised when column name cannot be found |
| ProjectDeletionFailed | Raised when Project deletion failed |
| DatasetDeletionFailed | Raised when Dataset deletion failed |
| DataDeletionFailed | Raises when Data deletion failed |
| UserAuthenticationFailed | Raised when User Authentication failed |
| DatasetInUse | Raised when Dataset is already in use by other user|