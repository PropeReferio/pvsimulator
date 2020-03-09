# Messaging app for Photovoltaic power and home power consumption

#### Built with Python 3.7, RabbitMQ 3.6, and Pika 1.1
#### One program generates a home power consumption value, and the other receives it, gets a Photovoltaic power value based on the hour, and outputs the sum. All of this is printed to the consoles. These values are written to a .csv file with a timestamp.

##### 1. Ensure that the following are installed on your computer:
1. python 3.7 (type "python --version" in the terminal)
2. rabbitmq 3.6.10 (type "sudo rabbitmqctl status" in the terminal, followed by your password)
3. pika 1.1.0 (Type "sudo pip install pika" in the terminal)

##### 2. Open two terminals, go to the directory containing homepowerproducer.py and homepowerconsumer.py.

##### 3. In one, type 'python3 homepowerproducer.py'. Messages will begin to send every 2 seconds.

##### 4. In the other, type 'python3 homepowerconsumer.py'. Messages will be received, and an output of the sum of the PV values and the home power consumption wattage will be printed.

##### 5. A wattage.csv file will be created. Feel free to open this as a spreadsheet, or use pandas to work with the data in a dataframe.

At any time in either terminal, press CTRL + C to stop the program.

