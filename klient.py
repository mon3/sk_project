import socket
import sys
import io

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.68.16.72', 8921)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)
while True:
    try:
        message = input()
        while len(message) != 0:
            # Send data
            sock.sendall(bytes(message, 'utf-8'))
        
            # Look for the response
            amount_received = 0
            amount_expected = len(message)
            data = sock.recv(6)
        
            print(len(message))
            amount_received += len(data)
            print ('received "%s"' % data)
            #message = input()
            sock.flush()
    
    finally:
        if(input() == "zamknij"):
            print ('closing socket')
            sock.close()