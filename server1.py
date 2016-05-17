# Save as server.py 
# Message Receiver
import os
import socket



host ="192.168.1.102"
port = 13009
buf = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
print "Waiting to receive messages..."

sock.listen(1)
conn, addr = sock.accept()
#i = 0
while True:
	# if (i=0):
	# 	text1 = "Podaj liczbe liter"
	# 	sock.sendto(data, addr)
	#connection, client_address = sock.accept()
	#i += 1
	data = conn.recv(buf)
	print "Received message: " + data
	if data == "exit":
		break
sock.close()

os._exit(0)
