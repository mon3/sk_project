import os
import socket
host = "192.168.0.10" # set to IP address of target computer
port = 13077
buf = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(addr)

print "WELCOME TO HANGMAN GAME by Monika and Karolina \n Read server's instructions carefully to avoid losing chances. \n Type 'exit' if you want to quit"
print "You're able to choose difficulty level: 1 - easy (10 chances), 2 - medium (8 chances), 3 - (6 chances) and the length of the word from 3 to 8 letters. \n"
print "Enjoy your game \n"
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
		# if (('bad' in data1) or ('good' in data1 ) or ('Good' in data1)):
		# 	data = " "
		# 	sock.sendto(data, addr)
		# 	print "wysylam: ", data
		# else:
		if ('?' in data1):

			data = raw_input()
			sock.sendto(data, addr)
			print "wysylam: ", data

		#sock.sendto(data, addr)
	if data == "exit":
		break
sock.close()
os._exit(0)