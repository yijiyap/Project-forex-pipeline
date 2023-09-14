# forex-pipeline

## Description
We will use Kafka and EC2. Rip my wallet

## Setup for Kafka
1. Install Kafka on the EC2 instance (make sure you change the security settings)
2. Open a new terminal, and start the Zookeeper server
```
cd kafka_2.12-3.5.1
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```
3. Open a new terminal, and run the EC2 instance
4. Allocate memory to the Kafka server
```
$ export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
```
5. Start the Kafka server
```
cd kafka_2.12-3.5.1
$ bin/kafka-server-start.sh config/server.properties
```
6. Create a topic in another terminal
```
$ bin/kafka-topics.sh --create --topic test1 --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```
7. Start a producer
```
$ bin/kafka-console-producer.sh --topic test1 --bootstrap-server 13.212.181.246:9092
```
8. New terminal, Start a consumer
```
$ bin/kafka-console-consumer.sh --topic test1 --bootstrap-server 13.212.181.246:9092
```

