from dotenv import load_dotenv
from kafka import KafkaConsumer
from json import loads, dumps
import json
from time import sleep
import pandas as pd
from s3fs import S3FileSystem

# Create a Kafka consumer
consumer = KafkaConsumer(
    'test1',
    bootstrap_servers=['13.212.114.151:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = S3FileSystem()

for count, i in enumerate(consumer):
    with s3.open('s3://kafka-forex-data/GBPUSD_{}.json'.format(count), 'w') as f:
        json.dump(i.value, f)