FROM python:3.9-slim

RUN pip install flask==1.1.2

WORKDIR /usr/src/app

COPY app/api.py api.py

ENV FLASK_APP=/usr/src/app/api.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=5000"]
