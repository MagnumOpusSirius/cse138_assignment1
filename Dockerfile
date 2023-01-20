FROM python:3.11.1-buster

WORKDIR /asgn1Dir
COPY . .

RUN pip install -r flaskV.txt

CMD ["flask","--app", "asgn1", "run", "--host=0.0.0.0", "--port=8081"]

