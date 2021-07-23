# postgresdb_ingester
Ingest millions of entries into PostgresDB using Python and SQLAlchemy

### Prerequisites:
1. Postgres Docker Container

* You can download and start postgres container using the following commands    
```
>> $ docker pull bitnami/postgresql:13.3.0-debian-10-r35    
>> $ docker run --name postgres -it -d --env-file=env.db -p 5432:5432 bitnami/postgresql:13.3.0-debian-10-r35
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
>> $ docker exec -it postgres bash
>> $ psql --username=admin --dbname=admin
>> admin=> \d employee;
>> admin=> select COUNT(*) from employee;
```
