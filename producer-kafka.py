from dotenv import load_dotenv
import pandas as pd
from kafka import KafkaProducer
import time
from json import dumps
import random

# Read the data from the csv file
df = pd.read_csv('GBPUSD.csv')

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=['13.212.114.151:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'))
# Send the data to the topic in a random interval of 1 to 5 seconds, up to 30 seconds
for index, row in df.iterrows():
    producer.send('test1', value=row.to_json())
    time.sleep(random.randint(1, 5))
    if index == 30:
        break

# producer.flush()