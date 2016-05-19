import os
import socket
host = "192.168.1.102" # set to IP address of target computer
port = 13046
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
		print "wysylam: ", data
		sock.sendto(data, addr)
	elif (i == 1):
		data1 = sock.recv(buf)
		print data1
		data = raw_input()
		print "wysylam: ", data
		i += 1
		sock.sendto(data, addr)
	else:
		#data = raw_input("Enter message to send or type 'exit': ")
		data1 = sock.recv(buf)
		print data1
		if (('bad' in data1) or ('good' in data1 ) or ('Good' in data1)):
			data = " Wcisnij Enter: "
			sock.sendto(data, addr)
			print "wysylam: ", data
		# else:
		data = raw_input()
		sock.sendto(data, addr)
		print "wysylam: ", data

		#sock.sendto(data, addr)
	if data == "exit":
		break
sock.close()
os._exit(0)