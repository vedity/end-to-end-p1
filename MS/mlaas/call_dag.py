from model_dag import create_pipeline

dag_name ="my_dag"
dag = create_pipeline(dag_name)
globals()["{}_dag".format(dag_name.lower())] = dag