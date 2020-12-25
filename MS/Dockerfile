FROM tiangolo/uwsgi-nginx-flask
COPY requirements.txt .
RUN pip install -r requirements.txt
#EXPOSE 5000
EXPOSE 8000
COPY mlaas /mlaas
WORKDIR /mlaas
