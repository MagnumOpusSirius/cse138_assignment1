FROM python:3.11.1-buster

WORKDIR /asgn1Dir

RUN pip install Flask==2.2.2

COPY . .

CMD ["python3", "-m", "flask", "--app", "run", "--host=0.0.0.0", "-p", "8081"]

