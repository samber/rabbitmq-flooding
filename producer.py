
import pika
import os
import random
import time


params = pika.URLParameters(os.environ["RABBITMQ_CONN"])
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"])

print("Producer starting. To exit press CTRL+C.")
while 1:
    channel.basic_publish(exchange=os.environ["RABBITMQ_EXCHANGE"], routing_key=os.environ["RABBITMQ_ROUTING_KEY"], body='Hello World!')
    print('*', end="")
    t = random.random() / 10
    time.sleep(t)
