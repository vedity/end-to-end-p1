import pandas as pd

class RemoveDuplicateRecordClass:
    """
    Parameters:
        subset: Subset takes a column or list of column label. It’s default value is none. After passing columns, it will consider them only for duplicates.
        keep: keep is to control how to consider duplicate value. It has only three distinct value and default is ‘first’.

            If ‘first’, it considers first value as unique and rest of the same values as duplicate.
            If ‘last’, it considers last value as unique and rest of the same values as duplicate.
            If False, it consider all of the same values as duplicates

        inplace: Boolean values, removes rows with duplicates if True.
        
    """
    def remove_duplicate_records(self,dataframe):
        dataframe.drop_duplicates(keep ='first',inplace=True)
        return dataframe