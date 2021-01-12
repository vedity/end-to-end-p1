FROM postgres:13.1
COPY init.sql /docker-entrypoint-initdb.d/
#RUN chmod -R 755 /docker-entrypoint-initdb.d/init.sql
#ENV POSTGRES_PASSWORD admin
#EXPOSE 5432