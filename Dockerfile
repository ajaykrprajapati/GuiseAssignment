
FROM python:3.8-alpine
MAINTAINER Ajay Kumar Prajapati

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /GUESSAI
WORKDIR /GUESSAI
COPY ./ /GUESSAI

RUN adduser -D user
User user
