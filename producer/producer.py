import time
import pika
import random
import string
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

EXCHANGE_NAME = 'json_exchange'
QUEUE_NAME = 'json_queue'
PUBLISH_FREQ = 100
MSG_BODY = '{{"payload": "{}"}}'.format(''.join(random.choice(string.ascii_letters) for _ in range(4096)))


def setup_rmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')
    channel.queue_declare(queue=QUEUE_NAME)
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME)

    return channel


def send_message(channel):
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='', body=MSG_BODY)


if __name__ == '__main__':
    rmq_channel = setup_rmq()

    while True:
        start_ts = time.time()
        send_message(rmq_channel)
        dt = time.time() - start_ts
        if dt < 1. / PUBLISH_FREQ:
            time.sleep(1. / PUBLISH_FREQ - dt)
        else:
            logger.warning('Publishing took {}s'.format(dt))