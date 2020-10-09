#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Enter The Host To Scan: ")

#prompt user for a port
#port = int(raw_input("[*] Enter The Port To Scan: "))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("Port %d is closed" % (port), 'red'))
	else:
		print(colored("Port %d is open" % (port), 'green'))

for port in range(1,100):
	portscanner(port)
