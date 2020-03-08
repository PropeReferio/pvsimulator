import time
import random
import pika
import csv

now = time.localtime()
hour = now[3]
meter = round(random.uniform(0,9001), 1)

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
    writer.writerow({'Timestamp': time.asctime(now), 'Meter (W)': meter, 'PV (kW)': pv,
    'Sum (W)': meter + pv *1000})
    #This is overwriting the file each time the program is run.