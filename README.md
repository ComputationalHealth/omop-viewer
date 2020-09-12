# omop-viewer

The viewer is designed to provide an open-sourced and scalable visualization tool to view patient chart and analytics data over ODSHI OMOP Common Data Model (CDM). To make it easy to replicate and launch, we have wrapped the work into an automated pipeline. 

Simply follow the steps below:

1. Clone this git;

2. On the highest level of omop-viewer/ folder, run 
      docker-compose build
   It will re-assemble the postgres database dump file which contains synthetic patient data in omop common data model

3. Then, run
       docker-compose up
       
4. To shut down the services, run
       docker-compose down

