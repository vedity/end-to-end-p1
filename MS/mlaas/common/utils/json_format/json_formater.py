def get_json_format(project_dataset_json,column_data):
    final_json_data=[]
    for x in project_dataset_json:
            outer_dict={}
            key_data=list(x.keys())
            value_data=list(x.values())
            for y in range(len(x)):
                if isinstance(value_data[y], list):
                    inner_json_data=[]
                    temp_dict={}
                    for j in value_data[y]:
                        inner_outer_dict={}
                        inner_key_data=list(j.keys())
                        inner_value_data=list(j.values())
                        for k in range(len(inner_key_data)):
                            if inner_key_data in column_data:
                                inside_inner_dict={ inner_key_data[k]:{
                                        "values": inner_value_data[k],
                                        "display":"false",
                                }}
                                inner_outer_dict.update(inside_inner_dict)
                            else:
                                inside_inner_dict={ inner_key_data[k]:{
                                        "values": inner_value_data[k],
                                        "display":"true",
                                }}
                                inner_outer_dict.update(inside_inner_dict)
                        temp_dict.update(inner_outer_dict)
                    inner_json_data.append(temp_dict)
                    inner_temp_dict={
                        key_data[y]:inner_json_data
                    }
                    outer_dict.update(inner_temp_dict)
                else:
                    if key_data[y] in column_data:
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
            final_json_data.append(outer_dict)
    return final_json_data


def get_Status_code(Status):
    status=Status
    status_code=status.split(",")[0].split(":")[1]
    status_msg=status.split(",")[1].split(":")[1]
    return status_code,status_msg

def menu_nested_format(dataset_json1,dataset_json2):
    column_data=['modulename','parentId','url']
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
    