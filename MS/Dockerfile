FROM tiangolo/uwsgi-nginx-flask
COPY requirements.txt .
RUN pip install -r requirements.txt
 
# # WORKDIR /opt/spark
# # # Get and install software
# # RUN apt -y upgrade && apt -y update 
# # RUN apt-get install -y default-jdk
# # RUN \
# #   #wget https://downloads.lightbend.com/scala/2.12.13/scala-2.12.13.tgz && \
# #   wget --no-check-certificate https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz 
# # RUN \
# #   #tar xvf scala-2.12.0.tgz && \
# #   #mv scala-2.12.0 /usr/local/scala && \ 
# #   tar xvf spark-3.0.1-bin-hadoop2.7.tgz
 
# # # Environment variables
# # ENV SPARK_HOME=/opt/spark/spark-3.0.1-bin-hadoop2.7 \
# #     PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
# # # Remove files from /opt/spark
# # RUN rm /opt/spark/*gz
# # # Set workDir
# # WORKDIR $SPARK_HOME/sbin
# # Start Spark
# CMD sh start-all.sh
EXPOSE 5000
EXPOSE 8000
EXPOSE 7000
COPY mlaas /mlaas
WORKDIR /mlaas