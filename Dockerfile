FROM python:3

RUN apt-get update
RUN apt-get update --fix-missing
RUN apt-get install -y apt-utils
RUN apt-get install -y python3-pip


ENV HOME /root

WORKDIR /root

COPY . .

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install bottle
RUN pip install bottle-mysql
RUN pip install mysqlclient
RUN pip install mysql-connector-python
RUN pip install gevent
RUN pip install gevent-websocket
RUN pip install bcrypt
ADD  https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait
CMD /wait && python -u backend/server.py