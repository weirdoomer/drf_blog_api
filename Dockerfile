FROM python:3.10.12-slim

WORKDIR /usr/src/drf_blog_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ARG uid
ARG username

RUN useradd -s /bin/bash -u ${uid} -U ${username} -m

USER ${username}