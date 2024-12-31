# rabbitmq - send message
import pika

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters("localhost", 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
message = "Hello, RabbitMQ!"
channel.basic_publish(exchange='', routing_key='hello', body=message)

print(f" [x] Sent '{message}'")

# Close the connection
connection.close()
