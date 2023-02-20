FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /master_personal
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
WORKDIR /Kindipro
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
