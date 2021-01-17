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