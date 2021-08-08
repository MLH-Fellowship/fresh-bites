FROM python:3.8-slim-buster

RUN mkdir /fresh-bytes
COPY requirements.txt /fresh-bytes
WORKDIR /fresh-bytes
RUN pip3 install -r requirements.txt

COPY . /fresh-bytes

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["sh" , "./entrypoint.sh"]