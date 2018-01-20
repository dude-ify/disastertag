FROM python:3.5
ENV PYTHONBUFFERED 1
RUN mkdir /config
ADD config/ /config/
RUN pip install -r /config/reqs.pip
RUN mkdir /src
WORKDIR /src
