# syntax=docker/dockerfile:1
FROM python:3.11.4-slim-buster
RUN apt update && apt install gcc -y
ENV PYTHONDONTWRITEBUTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/