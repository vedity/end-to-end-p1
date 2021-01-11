import datetime
from django.core.files.storage import FileSystemStorage

def save_file(user_name,dataset_visibility,file,file_path):
    """this function used to save the file uploaded by the user.file name will be append by the timestamp and 
    if the dataset_visibility is private save into user specific folder,else save into public folder. 

    Args:
            user_name[(String)]:[Name of the user]
            dataset_visibility[(String)]:[Name of Visibility public or private ]
            file_path[(string)] : [path string where we need to save file]
    return:
            [String]:[return name of the file]
    """
    if dataset_visibility.lower()=='private':
        file_path += user_name
    else:
        file_path += dataset_visibility
    fs = FileSystemStorage(location=file_path)
    file_name = file.name.split(".")[0]+ str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')) + '.csv'
    fs.save(file_name, file)
    return file_name
        

def get_Status_code(Status):
    """this function used to extract the status_code and status_msg from the string

    Args:
        Status[(String)]:[ value of status code and error message]
    return:
        [String,String]:[return extracted status_code ,status_msg]
    """
    status=Status 
    status_code=status.split(",")[0].split(":")[1]
    status_msg=status.split(",")[1].split(":")[1]
    return status_code,status_msg