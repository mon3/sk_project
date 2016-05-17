import os
import socket
host = "192.168.1.102" # set to IP address of target computer
port = 13009
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(addr)

while True:
    data = raw_input("Enter message to send or type 'exit': ")
    sock.sendto(data, addr)
    if data == "exit":
        break
sock.close()
os._exit(0)