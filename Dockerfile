FROM python:3.8-slim-buster

RUN mkdir /fresh-bites
COPY requirements.txt /fresh-bites
WORKDIR /fresh-bites
RUN pip3 install -r requirements.txt

COPY . /fresh-bites

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["sh" , "./entrypoint.sh"]
