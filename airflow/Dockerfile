FROM apache/airflow:2.0.1
WORKDIR /opt/airflow/
COPY requirements.txt .
COPY airflow.cfg .
RUN mkdir -p /opt/airflow/mlruns
RUN chmod -R 777 /opt/airflow/mlruns

USER 0
RUN apt-get update
RUN apt-get install -y build-essential

USER 50000
RUN pip install -r requirements.txt
