# HW-3-bigdata

## Kafka

## Запуск docker-compose

```
docker-compose build

docker-compose up -d

```

## Jobmanager

```
http://localhost:8081/#/overview
```

## Создание топиков (только 1 раз)

```
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic zitnerhw3 --partitions 3 --replication-factor 1

docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic zitnerhw3_processed --partitions 3 --replication-factor 1

```

## Команды для запуска джоб

```
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/device_job.py -d  

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/session_temp.py -d  

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/sliding_temp.py -d  

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/tumbling_temp.py -d  
```

## Описание топиков

```
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --describe zitnerhw3 

docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --describe zitnerhw3_processed 
```

## Блок 1

[Checkpoints local dir](./block_1)

```
python producer_1.py

python consumer_1.py

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/device_job.py -d
```

## Блок 2

[Flink Window](./block_2)

```
python producer_1.py

python consumer_2.py

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/session_temp.py -d 
```

### После проверки Session Window переходим к следующему шагу
```
cancel job in Apache Flink Dashboard

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/sliding_temp.py -d 
```

### После проверки Sliding Window переходим к следующему шагу
```
cancel job in Apache Flink Dashboard

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/sliding_temp.py -d 
```

### После проверки Tumbling Window переходим к следующему шагу
```
cancel job in Apache Flink Dashboard

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/jobs/tumbling_temp.py -d

cancel job in Apache Flink Dashboard
```

## Блок 3

```
stop python consumer_2.py

python failure.py
```
