# RabbitMQ flooding

Developed for cluster recovery testing.

## Start

Please set following environment variables:
- RABBITMQ_HOSTNAME
- RABBITMQ_PORT
- RABBITMQ_USERNAME
- RABBITMQ_PASSWORD
- RABBITMQ_VHOST
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
       -e RABBITMQ_PORT=5672 \
       -e RABBITMQ_USERNAME=guest \
       -e RABBITMQ_PASSWORD=guest \
       -e RABBITMQ_VHOST=/ \
       -e RABBITMQ_QUEUE=hello \
       -e RABBITMQ_EXCHANGE= \
       -e RABBITMQ_ROUTING_KEY=hello \
       samber/rabbitmq-flooding:latest consumer.py
# and
docker run --rm -i \
       -e RABBITMQ_HOSTNAME=rabbitmq \
       -e RABBITMQ_PORT=5672 \
       -e RABBITMQ_USERNAME=guest \
       -e RABBITMQ_PASSWORD=guest \
       -e RABBITMQ_VHOST=/ \
       -e RABBITMQ_QUEUE=hello \
       -e RABBITMQ_EXCHANGE= \
       -e RABBITMQ_ROUTING_KEY=hello \
       samber/rabbitmq-flooding:latest producer.py
```
