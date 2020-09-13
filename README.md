# omop-viewer

The viewer is designed to provide an open-sourced and scalable visualization tool to view patient chart and analytics data over ODSHI OMOP Common Data Model (CDM). To make it easy to replicate and launch, we have wrapped the work into an automated pipeline. 

Author: Guannan Gong (guannan.gong@yale.edu)

## Installation
Simply follow the steps below:

1. Clone this git;

2. On the highest level of omop-viewer/ folder, run 
```bash
      docker-compose build
```
   It will re-assemble the postgres database dump file which contains synthetic patient data in omop common data model

3. Then, run
```bash
       docker-compose up -d db
```
This will start the database docker container, then run

```bash
       docker-compose up -d app
```
This will start the Django app container

4. Open a web browser, and go 
```bash
      http://localhost:5599/patViewer/
```

5. To shut down the services, run
       docker-compose down

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
