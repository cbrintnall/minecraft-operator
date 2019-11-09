FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/*.py /app

CMD [ "kopf", "run", "--standalone", "/app/main.py" ]

