FROM postgres:13.1
COPY init.sql /docker-entrypoint-initdb.d/
COPY pg_hba.conf /var/lib/postgresql/data/
RUN chmod -R 755 /docker-entrypoint-initdb.d/init.sql
#ENV POSTGRES_PASSWORD postgres
#EXPOSE 5432