'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Jay Shukla         26-April-2021           1.0           Created Class
 
*/
'''

#* Library Imports
import logging

#* Commong Utilities
from common.utils.logger_handler import custom_logger as cl

#* Defining Logger
user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('change_datatype')

class ChangeDatatype:

    def detect_datetime(self, schema_id, dataset_id, format):
        pass
