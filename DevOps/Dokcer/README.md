# docker images:

## mysql:8.0

### how to access?
docker exec -it <mysql-container-id> mysql -u user_name -p

run as mysql:
USE db_name;
SELECT * FROM query_log;

## jenkins:2.414.2-jdk11
### how to access?
docker exec -it <jenkins-container-id> bash

