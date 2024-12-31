import pika

# Connection parameters
credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters("localhost", 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare the queue (ensures it exists)
channel.queue_declare(queue='hello')

# Callback function to process messages
def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

# Set up consumption
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()