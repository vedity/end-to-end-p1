FROM puckel/docker-airflow

WORKDIR /usr/local/airflow/
COPY requirements.txt .
COPY airflow.cfg .
RUN pip install --user -r requirements.txt

