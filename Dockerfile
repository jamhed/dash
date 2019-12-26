FROM python:buster

RUN pip install dash numpy pandas sklearn gunicorn
COPY app.py app.py

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0", "app:server"]
