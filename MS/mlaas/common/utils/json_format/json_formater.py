def get_json_format(project_dataset_json,column_data):
    """this function used to create a predefined json format where column_data argument will have list
        of column which has to be Display key should be false.
    
    Args:
        project_dataset_json[(list)]:[list of dictonery.]
        column_data[(String)] :[name of the column.]
    return:
        [list] : [list of dictonery]
    """
    final_json_data=[]
    for x in project_dataset_json: #get dict object into a list of object
            outer_dict={} 
            key_data=list(x.keys()) # get first list of dictonery key's and convert into list
            value_data=list(x.values()) # get first list of dictonery value's and convert into list
            for y in range(len(x)):
                if isinstance(value_data[y], list): #checking if key has the value List object instace
                    inner_json_data=[]
                    temp_dict={}
                    for j in value_data[y]: #get the list of dictonery
                        inner_outer_dict={} 
                        inner_key_data=list(j.keys()) #get dictonery key's and convert into list
                        inner_value_data=list(j.values())  #get dictonery value's and convert into list
                        for k in range(len(inner_key_data)):
                            if inner_key_data in column_data: #checking column_data values if present then its display key should be false otherwise True
                                inside_inner_dict={ inner_key_data[k]:{
                                        "values": inner_value_data[k],
                                        "display":"false",
                                }}
                                inner_outer_dict.update(inside_inner_dict) #merge the dictonery with  inside_inner_dict 
                            else:
                                inside_inner_dict={ inner_key_data[k]:{
                                        "values": inner_value_data[k],
                                        "display":"true",
                                }}
                                inner_outer_dict.update(inside_inner_dict) #merge the dictonery with  inside_inner_dict
                        temp_dict.update(inner_outer_dict) #merge the inner_outer_dict with the outer function temp_dict dictonery
                    inner_json_data.append(temp_dict) # temp_dict append with the inner_json_data list
                    inner_temp_dict={     #inner_json_data list assign as the value of key_data[y]
                        key_data[y]:inner_json_data
                    }
                    outer_dict.update(inner_temp_dict) #inner_temp_dict merge with the main outer_dict dictonery
                else:
                    if key_data[y] in column_data: #checking column_data values if present then its display key should be false otherwise True
                        inner_dict={ key_data[y]:{
                                "values":value_data[y],
                                "display":"false",
                        }}
                        outer_dict.update(inner_dict)
                    else:
                        inner_dict={ key_data[y]:{
                                "values":value_data[y],
                                "display":"true",
                        }}
                        outer_dict.update(inner_dict)
            final_json_data.append(outer_dict) #final outer_dict dictonery append into final_json_data list
    return final_json_data #return custom format data

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

def menu_nested_format(dataset_json1,dataset_json2):
    """this function used to create predefind jsonformat where multiple list of dictonery has been passed.

    Args:
        dataset_json1 [(list)] : [list of dictonery with column and records]
        dataset_json2 [(list)] : [list of dictonery with column and records]
    return:
        [list] :[list of dictonery]
    """
    column_data=['modulename','parentId','link']
    inside_column_data=['icon','modulename']
    json_data=[]
    json_data1=[]
    json_data2=[]
    for x in dataset_json1:
        outer_dict={}
        for y in dataset_json2: 
            if x["id"]==y["parentId"]:  
                y_keys=list(y.keys())
                y_data=list(y.values())
                inner_dict={}
                for i in range(len(y_keys)):
                    if y_keys[i] not in inside_column_data:
                        inner_dict.update({y_keys[i]:y_data[i]})
                json_data.append(inner_dict)
        x_keys=list(x.keys())
        x_data=list(x.values())
        for j in range(len(x_keys)):
            if x_keys[j] not in column_data:
                outer_dict.update({x_keys[j]:x_data[j]})
        outer_dict.update({"subItems":json_data})
        json_data1.append(outer_dict)
        json_data=[]
    json_data1.insert(0,{"id": 1,
        "label": 'MENU',
        "isTitle": 'true'
    })

    return json_data1

def get_column_name(column_name):
    json_list=[]
    column_list = list(column_name[0].keys())
    for i in column_list:
        temp_dict ={
            "data" : i
        }
        json_list.append(temp_dict)
    return json_list

def get_schema_format(column_name,predicted_datatype):
    json_data = []
    for x in range(1,len(column_name)):
        temp_dict = {
            "column_name": column_name[x],
            "data_type": predicted_datatype[x],
            "column_attribute":"",
            "change_column_name":"",
        }
        json_data.append(temp_dict)
    return json_data

    
