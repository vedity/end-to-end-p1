FROM puckel/docker-airflow

WORKDIR /usr/local/airflow/
COPY requirements.txt .
COPY airflow.cfg .
RUN pip install -r requirements.txt
USER 0
RUN pip install -r requirements.txt
USER 1000

