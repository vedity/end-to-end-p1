'''
/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------
 Vipul Prajapati      25-JAN-2021           1.0           Initial Version 
 
*/
'''


import pandas as pd


class BasicParameterClass:
    
    def __init__(self,model_mode,split_method,cv,train_size,test_size,valid_size):
        
        self.model_mode = model_mode
        self.split_method = split_method
        
        self.cv = cv

        self.train_size = train_size
        self.test_size = test_size
        self.valid_size = valid_size
        

    def get_split_parameter(self):
        
        if self.model_mode == 'Auto':
            
            train_size = 0.8
            test_size = 0.2
            cv = 5
            
        else:
            if self.split_method == 'holdout':
                
                train_size = self.train_size
                test_size = self.test_size
                valid_size = self.valid_size
                
            else:
                train_size = self.train_size
                test_size = self.test_size
                cv = self.cv
                
        return train_size,test_size,valid_size,cv
    
   
   
    