FROM python:buster

RUN pip install dash
RUN pip install numpy
RUN pip install pandas
RUN pip install sklearn
RUN pip install gunicorn
COPY app.py app.py

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0", "app:server"]
