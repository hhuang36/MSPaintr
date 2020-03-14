FROM ubuntu:18.04

RUN apt-get update
RUN apt-get update --fix-missing
RUN apt-get install -y apt-utils
RUN apt-get install -y python3

ENV HOME /root

WORKDIR /root

COPY . .

EXPOSE 8000

RUN apt-get install -y python-bottle

CMD ["python", "backend/server.py"]