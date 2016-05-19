import os
import socket
host = "192.168.1.102" # set to IP address of target computer
port = 13025
buf = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(addr)

i = 0 
while True:
	if (i == 0):
		data1 = sock.recv(buf)
		print data1
		data = raw_input()
		i += 1
	elif (i == 1):
		data1 = sock.recv(buf)
		print data1
		data = raw_input()
		i += 1
	else:
		data = raw_input("Enter message to send or type 'exit': ")
	sock.sendto(data, addr)
	if data == "exit":
		break
sock.close()
os._exit(0)