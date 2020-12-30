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
    