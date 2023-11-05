FROM python:3.10.4

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requierments.txt /usr/src/app/

RUN pip install -r requierments.txt

COPY ./../../.. /usr/src/app/

#COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/usr/src/app/docker/images/python/entrypoint.sh"]
