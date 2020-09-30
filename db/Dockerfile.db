FROM postgres
LABEL Guannan Gong <guannan.gong@yale.edu>

RUN mkdir /omop
COPY ./data/omop/ /omop
WORKDIR /omop

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install wget

# Download omop sql dump files to /omop
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_aa.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_ab.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_ac.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_ad.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_ae.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_af.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_ag.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_ah.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_ai.sql
RUN wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop_aj.sql

# Re-construct the original omop sql dump file
RUN cat synthea_omop_**.sql > /docker-entrypoint-initdb.d/synthea_omop_dump.sql