echo "Initiatilizing OMOP data..."

cd /omop
wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop.tar
tar -xzvf synthea_omop.tar && rm -rf synthea_omop.tar
cat synthea_omop_**.sql > /docker-entrypoint-initdb.d/synthea_omop_dump.sql
rm -f *.sql
