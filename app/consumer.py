# consumer.py
import pika, json

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='signal_queue')

    def callback(ch, method, properties, body):
        payload = json.loads(body)
        print("📥 Received:", payload)

    channel.basic_consume(queue='signal_queue', on_message_callback=callback, auto_ack=True)
    print("🚀 Waiting for messages...")
    channel.start_consuming()
