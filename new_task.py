#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='dowork', durable=True) #Name of queue

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='dowork', #Name of queue goes here
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent, gets
                          #saved to disk or cache. This isn't foolproof, as 
                          # there is a
                          #short time window in between receiving a message
                          #and saving it. Publisher confirms are a stronger
                          #guarantee.
                      ))
print(" [x] Sent %r" % message)

connection.close()