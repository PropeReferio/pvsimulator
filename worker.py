import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='dowork', durable=True) #durable means that even 
#if the server goes down, messages aren't lost.

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))#Fakes a 1 second delay per dot in the message
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag) #This is to make sure 
    #messages aren't lost if a worker is killed

channel.basic_consume(queue='dowork',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()