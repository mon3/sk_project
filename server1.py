# Save as server.py 
# Message Receiver
import os
import socket



host ="192.168.1.102"
port = 13020
buf = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
print "Waiting to receive messages..."

sock.listen(1)
conn, addr = sock.accept()
i = 0
data = []
while True:
	if (i == 0):
		text1 = "Podaj liczbe liter"
		conn.sendall(text1)
		i += 1
	elif (i == 1):
		text1 = "Wybierz poziom: A, B, C"
		conn.sendall(text1)
		i += 1
	else:
		
		data = conn.recv(buf)
		print "Received message: " + data

	if data == "exit":
		break
sock.close()

os._exit(0)
