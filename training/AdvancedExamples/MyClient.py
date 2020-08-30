# This is for the client testing
import socket

s = socket.socket() #Create a socket object

HOST = 'localhost'
PORT = 15202

s.connect((HOST, PORT))
print(s.recv(1024))
s.close