
import pika
import os
import random
import time

credentials = pika.PlainCredentials(
    os.environ["RABBITMQ_USERNAME"],
    os.environ["RABBITMQ_PASSWORD"]
)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    os.environ["RABBITMQ_HOSTNAME"],
    os.environ["RABBITMQ_PORT"],
    os.environ["RABBITMQ_VHOST"],
    credentials,
))
channel = connection.channel()

channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"])

print("Producer starting. To exit press CTRL+C.")
while 1:
    channel.basic_publish(exchange=os.environ["RABBITMQ_EXCHANGE"], routing_key=os.environ["RABBITMQ_ROUTING_KEY"], body='Hello World!')
    print('*', end="")
    t = random.random() / 10
    time.sleep(t)
