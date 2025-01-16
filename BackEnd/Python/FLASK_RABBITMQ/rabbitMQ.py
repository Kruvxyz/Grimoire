import json
import os
import pika
import time
from logger_config import logger
from pika.adapters.blocking_connection import BlockingConnection
from typing import Dict


def get_connection() -> BlockingConnection:
    TOTAL_ATTEMPTS = 5
    TIME_BETWEEN_ATTEMPTS = 5
    user = os.environ.get("RABBITMQ_USER")
    password = os.environ.get("RABBITMQ_PASS")
    host = os.environ.get("RABBITMQ_HOST")
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(host, 5672, '/', credentials)
    for attempt in range(TOTAL_ATTEMPTS):  # Retry 
        try:
            connection = pika.BlockingConnection(parameters)
            logger.info(f"Connected to RabbitMQ")
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            logger.info(f"Attempt {attempt}/{TOTAL_ATTEMPTS} | Connection failed: {e}. Retrying in {TIME_BETWEEN_ATTEMPTS} seconds...")
            time.sleep(TIME_BETWEEN_ATTEMPTS)

    raise Exception("Failed to connect to RabbitMQ after 5 attempts")

def send_message(queue_name: str, message: Dict[str, str]) -> None:
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(
        exchange='', 
        routing_key=queue_name, 
        body=json.dumps(message)
    )
    connection.close()
