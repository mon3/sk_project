import socket
import sys


HOST = '192.168.1.102 '
PORT = 8921
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print ( 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print  ('sending "%s"' % message)
    sock.sendall(bytes(message,'utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print ( 'received "%s"' % data)

finally:
    print  ('closing socket')
    sock.close()