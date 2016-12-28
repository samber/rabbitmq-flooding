# RabbitMQ flooding

Developed for cluster recovery testing.

## Start

Please set following environment variables:
- RABBITMQ_HOSTNAME
- RABBITMQ_QUEUE
- RABBITMQ_EXCHANGE
- RABBITMQ_ROUTING_KEY

```sh
docker-compose up -d
docker-compose scale producer=10 consumer=10
docker-compose logs -f

# or

docker run --rm -i \
       -e RABBITMQ_HOSTNAME=rabbitmq \
       -e RABBITMQ_QUEUE=hello \
       samber/rabbitmq-flooding:latest consumer.py
# and
docker run --rm -i \
       -e RABBITMQ_HOSTNAME=rabbitmq \
       -e RABBITMQ_QUEUE=hello \
       -e RABBITMQ_EXCHANGE= \
       -e RABBITMQ_ROUTING_KEY= \
       samber/rabbitmq-flooding:latest producer.py
```