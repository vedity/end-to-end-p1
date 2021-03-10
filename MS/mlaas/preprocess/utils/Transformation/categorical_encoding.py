
#* Importing Libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

class EncodeClass:
    
    # def label_encoding(self, series):

    #     labelencoder = LabelEncoder()

    #     series = labelencoder.fit_transform(series)
        
    #     return series

    def label_encoding(self,DBObject,connection,column_list, table_name,col_lst):
        '''
        Encoding Related Functions.
        '''
        try:
            sql_command = "update {table_name} m SET '{column_list[1]}' = WANT_THIS from (SELECT  index, dense_rank() OVER ( ORDER BY '{column_list[1]}') AS WANT_THIS FROM {table_name}) s where m.'{column_list[0]}' = s.{column_list[0]};"
            logging.info("label_encoding logging"+str(sql_command))
            label_df = DBObject.update_record(connection,sql_command)
            return label_df

        except Exception as exc:
                return exc
        
    def one_hot_encoding(self, series):
        
        df = pd.DataFrame(series)
        col_name = series.name
    
        enc = OneHotEncoder(handle_unknown='ignore')

        ohe_df = enc.fit_transform(df).toarray()
        enc_df = pd.DataFrame(ohe_df, columns = [f"{col_name}_{i}" for i in range(ohe_df.shape[1])])

        return enc_df

