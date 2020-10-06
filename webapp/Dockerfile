FROM python:3.7
LABEL Guannan Gong <guannan.gong@yale.edu>

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
COPY ./src /app

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

CMD /bin/sh -c "python /app/manage.py runserver 0.0.0.0:8000"
