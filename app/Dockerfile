FROM python:3.7
LABEL Guannan Gong <guannan.gong@yale.edu>

ENV PYTHONUNBUFFERED 1

COPY ./app/requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

## Add the wait script to the image
#ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
#RUN chmod +x /wait

#RUN groupadd  --gid 1907360257 postgres
#RUN useradd -l --uid 1907442394 --gid 1907360257 -d /app -g postgres -m postgres 
#USER postgres