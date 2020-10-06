FROM postgres:13.0
LABEL Guannan Gong <guannan.gong@yale.edu>

RUN apt-get -qyy update && \
    apt-get -qyy upgrade && \
    apt-get -qyy install wget

RUN mkdir -p /omop
WORKDIR /omop
COPY load_data.sh /omop/
RUN chmod 775 /omop/load_data.sh
