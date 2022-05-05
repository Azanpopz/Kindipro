FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /deleterobot
WORKDIR /deleterobot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]


FROM ghcr.io/breakdowns/mega-sdk-python:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .

CMD ["python3", "kang.py"]
