import csv

with open('wattage.csv', mode='w') as watt_file:
    fieldnames = ['Timestamp', 'Meter', 'PV', 'Sum']
    writer = csv.DictWriter(watt_file, fieldnames=fieldnames)

    writer.writeheader() #These are the fieldnames
    writer.writerow({'Timestamp': time.localtime(), 'Meter': random.uniform(0,9001), 'PV': 'Summer'})
    #This is overwriting the file each time the program is run.