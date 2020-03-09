1. Ensure that the following are installed on your computer:
	python 3.8 (type "python --version" in the terminal)
	rabbitmq 3.6.10 (type "sudo rabbitmqctl status" in the terminal, followed by your password)
	pika 1.1.0 (Type "sudo pip install pika" in the terminal)

1. Open two terminals.
2. In one, type 'python homepowerproducer.py'. Messages will begin to send every 2 seconds.
3. In the other, type 'python homepowerconsumer.py'. Messages will be received, and an output of the sum of the PV values and the home power consumption wattage will be printed.
4. A wattage.csv file will be created. Feel free to open this as a spreadsheet, or use pandas to work with the data in a dataframe.

