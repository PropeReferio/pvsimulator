#!/usr/bin/env python
import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='homepower', durable=True) #Name of queue

while True: #Messages will send every 2 seconds until the process is killed.
    message = str(round(random.uniform(0,9001), 1))#Body accepts string
    channel.basic_publish(exchange='',
                        routing_key='homepower', #Name of queue goes here
                        body=message,
                        properties=pika.BasicProperties(
                            delivery_mode = 2 # make message persistent, gets
                            #saved to disk or cache. This isn't foolproof, as 
                            # there is a
                            #short time window in between receiving a message
                            #and saving it. Publisher confirms are a stronger
                            #guarantee.
                        ))
    print(" [x] Sent %r" % message)
    time.sleep(2.0)

connection.close()