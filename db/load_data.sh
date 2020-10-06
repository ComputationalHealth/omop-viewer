echo "Initiatilizing OMOP data..."

cd /omop
wget https://cch-omop-viewer.s3.amazonaws.com/synthea_omop.tar
tar -xzvf synthea_omop.tar && rm -rf synthea_omop.tar
psql --user postgres -f synthea_omop.sql omop
rm -f *.sql
