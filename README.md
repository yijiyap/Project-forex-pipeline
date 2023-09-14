# forex-pipeline
Used Kafka, EC2, and Python to create a forex pipeline. 
Would have used an API to get the data, but I didn't want to pay for it. As such I used a csv file instead.

## Description
The forex pipeline is a simple pipeline that takes in forex data from a csv file, and sends it to a Kafka server.

Note: 
- Each time you update start and stop the EC2 instance, you will need to change the IP address in the code
- You will have to go to `sudo nano config/server.properties` and change the ADVERTISED_LISTENERS to the EC2 instance's IP address

## Setup for Kafka
1. Install Kafka on the EC2 instance (make sure you change the security settings)
2. Open a new terminal, and start the Zookeeper server
```
cd kafka_2.12-3.5.1
bin/zookeeper-server-start.sh config/zookeeper.properties
```
3. Open a new terminal, and run the EC2 instance
4. Allocate memory to the Kafka server
```
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
```
5. Start the Kafka server
```
cd kafka_2.12-3.5.1
bin/kafka-server-start.sh config/server.properties
```
6. Create a topic in another terminal
```
bin/kafka-topics.sh --create --topic test1 --bootstrap-server 13.212.114.151:9092 --replication-factor 1 --partitions 1
```
7. Start a producer
```
bin/kafka-console-producer.sh --topic test1 --bootstrap-server 13.212.114.151:9092
```
8. New terminal, Start a consumer
```
bin/kafka-console-consumer.sh --topic test1 --bootstrap-server 13.212.114.151:9092
```

