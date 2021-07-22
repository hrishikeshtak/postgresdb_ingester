# postgresdb_ingester
Ingest millions of entries into PostgresDB using Python and SQLAlchemy

### Prerequisites:
1. Postgres Docker Container

* You can download and start postgres container using the following commands    
```
>> $ docker pull bitnami/postgresql:13.3.0-debian-10-r35    
>> $ docker run --name postgresql -it -d -e POSTGRESQL_USERNAME=my_user -e POSTGRESQL_PASSWORD=password123 -e POSTGRESQL_DATABASE=my_database -p 5432:5432 bitnami/postgresql:13.3.0-debian-10-r35
```

2. Download required python dependencies    

```
>> $ python3.8 -m venv venv
>> $ source venv/bin/activate
>> $ pip3 install -r requirements.txt
```

### How to run python script:
Note: Script will ingest millions of employee records into employee table, it will take few minutes to complete.
```
>> $ python3 ingest_millions_into_pgsql.py
```

* Use the following commands to enter into postgres container and check tables entries    
```
>> $ docker exec -it postgresql bash
>> $ psql --username=my_user --dbname=my_database
>> my_database=> \d employee;
>> my_database=> select COUNT(*) from employee;
```
