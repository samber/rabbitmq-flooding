
import pika
import os
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ["RABBITMQ_HOSTNAME"]))
channel = connection.channel()

channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"])

def callback(ch, method, properties, body):
    print('*', end="")

print("Consumer starting. To exit press CTRL+C.")
channel.basic_consume(callback, queue=os.environ["RABBITMQ_QUEUE"], no_ack=True)
channel.start_consuming()
