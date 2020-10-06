# omop-viewer

The viewer is designed to provide an open-sourced and scalable visualization tool to view patient chart and analytics data over ODSHI OMOP Common Data Model (CDM). To make it easy to replicate and launch, we have wrapped the work into an automated pipeline. 

*Author: Guannan Gong (guannan.gong@yale.edu)*

## Installation
Simply follow the steps below:

1. Clone this git;

2. Run docker-compose to launch the environment
```bash
      docker-compose up -d --build
```

3. On the first run, download S3 data with an export of OMOP database (including vocabulary) and load to postgres (NOTE: this will download ~1.5 GB compressed data, uncompress to ~11 GB total, load the database, and then remove the source files, requiring ~20-25 GB of space transiently and ~10-15 GB after for the container running postgres):
```bash
       docker exec omop-viewer_db_1 /bin/sh /omop/load_data.sh
```

4. Open a web browser, and go 
```bash
      http://localhost:5599
```

5. To shut down the services, run
       docker-compose down -v

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
