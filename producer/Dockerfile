# vim:set ft=dockerfile:
FROM debian:stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential python3-wheel \
	python3 python3-pip python3-dev python3-setuptools

COPY requirements.txt /usr/local/producer/
WORKDIR /usr/local/producer/
RUN pip3 install -r requirements.txt

COPY . /usr/local/producer/
WORKDIR /usr/local/producer/

CMD python3 producer.py
