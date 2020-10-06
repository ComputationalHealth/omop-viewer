FROM python:3.7
LABEL Guannan Gong <guannan.gong@yale.edu>

ENV PYTHONUNBUFFERED 1

RUN apt-get -qyy update && \
    apt-get -qyy upgrade && \
    apt-get -qyy install netcat

RUN mkdir -p /app
COPY ./src /app

RUN pip install --upgrade pip && pip install -r /app/requirements.txt
COPY wait_db.sh .
RUN chmod +x wait_db.sh

CMD ./wait_db.sh && /bin/sh -c "python /app/manage.py runserver 0.0.0.0:8000"
