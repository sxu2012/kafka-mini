
# generator/app.py
import json
import os
# kafka python library
from kafka import KafkaProducer
from time import sleep
#transactions.py
from transactions import create_random_transaction

#Kafka Python's producer API: https://github.com/dpkp/kafka-python#kafkaproducer
#KafkaProducer use this URL to bootstrap their connection to the kafka cluster

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
TRANSACTIONS_PER_SECOND = float(os.environ.get('TRANSACTIONS_PER_SECOND'))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == '__main__':
    #producer send messages to TRANSACTIONS_TOPIC
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode()
    )
    while True:
        transaction = create_random_transaction()
        # message = json.dumps(transaction)
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction) # debug
        sleep(SLEEP_TIME)