import pika
import time
import random
import csv

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='homepower', durable=True) #durable means that even 
#if the server goes down, messages aren't lost.

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag) #This is to make sure 
    #messages aren't lost if a consumer is killed
    now = time.localtime()
    hour = now[3]
    meter = float(body) #Change this to values from message received

    if hour <= 5:
        pv = 0
    elif hour == 6:
        pv = 0.1
    elif hour == 7:
        pv = 0.2
    elif hour == 8:
        pv = 0.4
    elif hour == 9:
        pv = 0.6
    elif hour == 10:
        pv = 1.7
    elif hour == 11:
        pv = 2.3
    elif hour == 12:
        pv = 2.8
    elif hour == 13:
        pv = 3.1
    elif hour == 14:
        pv = 3.3
    elif hour == 15:
        pv = 3.2
    elif hour == 16:
        pv = 3.0
    elif hour == 17:
        pv = 2.5
    elif hour == 18:
        pv = 1.9
    elif hour == 19:
        pv = 0.6
    elif hour == 20:
        pv = 0.1
    else:
        pv = 0

    with open('wattage.csv', mode='w') as watt_file:
        fieldnames = ['Timestamp', 'Meter (W)', 'PV (kW)', 'Sum (W)']
        writer = csv.DictWriter(watt_file, fieldnames=fieldnames)

        writer.writeheader() #These are the fieldnames
        writer.writerow({'Timestamp': time.asctime(now), 'Meter (W)': meter, 
        'PV (kW)': pv, 'Sum (W)': meter + pv * 1000})
        #This is overwriting the file each time the program is run.
    print('Values written to power log.')

channel.basic_consume(queue='homepower',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


#I think everything below this line needs to go inside the callback function
