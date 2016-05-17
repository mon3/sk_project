import socket
import sys

	# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '192.168.1.102 '
PORT = 8921

	# Bind the socket to the port
server_address = (HOST, PORT)
print ( 'starting up on %s port %s' % server_address)
sock.bind(server_address)

	# Listen for incoming connections
sock.listen(1)



while True:
    # Wait for a connection
    print ( 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print ( 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        data = connection.recv(6)
        while (len(data) !=0):
        	print ( 'received "%s"' % data)
        	# if data:
        	data1 = input()
        	print ('sending data back to the client')
        	connection.sendall(bytes(data1,'utf-8'))
        	# else:
        	# 	print ( 'no more data from', client_address)
        	# 	break
            
    finally:
        # Clean up the connection
        connection.close()
