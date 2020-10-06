FROM postgres
LABEL Guannan Gong <guannan.gong@yale.edu>

RUN apt-get -qyy update && \
    apt-get -qyy upgrade && \
    apt-get -qyy install wget

RUN mkdir /omop
COPY ./data/omop/ /omop
WORKDIR /omop

# Download omop sql dump files to /omop
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop.tar && \
    tar -xzvf synthea_omop.tar && rm -rf synthea_omop.tar && \
    cat synthea_omop_**.sql > /docker-entrypoint-initdb.d/synthea_omop_dump.sql && \
    rm -f *.sql
