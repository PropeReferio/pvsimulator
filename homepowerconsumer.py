#!/usr/bin/env python
import pika
import time
import random
import csv
import os.path

powertime = { #The keys are hours, the values are the kW values provided for
              #the assignment.
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0.1,
    7: 0.2,
    8: 0.4,
    9: 0.6,
    10: 1.7,
    11: 2.3,
    12: 2.8,
    13: 3.1,
    14: 3.3,
    15: 3.2,
    16: 3.0,
    17: 2.5,
    18: 1.9,
    19: 0.6,
    20: 0.1,
    21: 0,
    22: 0,
    23: 0,
    24: 0
}

def log_values(meter):
    pv = powertime[time.localtime()[3]] #Uses the current hour as a key
        #to get a kW value
    if os.path.isfile('wattage.csv'): #appends to file if it exists already
        with open('wattage.csv', mode='a') as watt_file:
            writer = csv.writer(watt_file, delimiter=',')
            writer.writerow([time.asctime(), meter, pv, meter + pv *1000])
    else: #Creates the file with headers if it doesn't exist yet
        with open('wattage.csv', mode='w') as watt_file:
            fieldnames = ['Timestamp', 'Meter (W)', 'PV (kW)', 'Sum (W)']
            writer = csv.DictWriter(watt_file, fieldnames=fieldnames)
            writer.writeheader()
    
    print('Values written to power log.')
    print(f"Sum of Photovoltaic power values and home power consumption: \
{pv * 1000 + meter} watts.")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='homepower', durable=True) #durable means that 
#even if the server goes down, messages aren't lost.

def callback(ch, method, properties, body):
    print(" [x] Received message: %r watts." % float(body))
    ch.basic_ack(delivery_tag = method.delivery_tag) #This is to make sure 
    #messages aren't lost if a consumer is killed
    log_values(float(body))
    

channel.basic_consume(queue='homepower',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()