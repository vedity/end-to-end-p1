from pyspark import SparkContext, SparkConf
from pyspark.sql import DataFrameReader, SQLContext
import os

sparkClassPath = os.getenv('SPARK_CLASSPATH', 'postgresql-42.2.6.jar')
conf = SparkConf()
conf.setAppName('application')
conf.set('spark.jars', 'file:%s' % sparkClassPath)
conf.set('spark.executor.extraClassPath', sparkClassPath)
conf.set('spark.driver.extraClassPath', sparkClassPath)
# Uncomment line below and modify ip address if you need to use cluster on different IP address
#conf.set('spark.master', 'spark://127.0.0.1:7077')

sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

url = 'postgresql://localhost:5432/postgresql'
properties = {'user':'airflow', 'password':'airflow'}

# df = DataFrameReader(sqlContext).jdbc(url='jdbc:%s' % url, table='mlaas.activity_tbl', properties=properties)
url= "jdbc:postgresql://postgresql:5432/airflow?user=airflow&password=airflow"
df=sqlContext.read.format("jdbc").option("url",url).option("dbtable","alembic_version").load()
df.printSchema()
df.show()