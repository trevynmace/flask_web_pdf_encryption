FROM python:3.7-alpine

MAINTAINER Trevyn Mace "trevynmace@gmail.com"

#Don't need these two commands because we're using python:3.7-alpine image as our base image
#RUN apt-get update -y && \
#    apt-get install -y python-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]