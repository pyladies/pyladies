FROM python:2.7-slim
COPY requirements.txt /
COPY entrypoint.sh /

RUN apt-get update
RUN apt-get -y install gcc

RUN pip install -r /requirements.txt

COPY www /www
WORKDIR /www

EXPOSE 8080
ENTRYPOINT ["/entrypoint.sh"]