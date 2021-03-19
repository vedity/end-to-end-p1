FROM riddhiisg123/spark:v1
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.6.jar
ENV SPARK_CLASSPATH=/opt/spark/postgresql-42.2.6.jar
COPY mlaas /mlaas
WORKDIR /mlaas
