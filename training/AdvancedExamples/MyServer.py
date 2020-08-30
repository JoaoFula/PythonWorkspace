# Create a simple server
from socket import *
from time import ctime
from threading import Thread

class client_handler(Thread):
    #Handles a client request
    def __init__(self, client):
        Thread.__init__(self)
        self._client = client

    def run(self):
        self._client.send(bytes(ctime() + ' Have a nice day', 'ascii'))
        self._client.close()

HOST = 'localhost'
PORT = 15202
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
# Server waits for connection and hands over sockets to client handlers
while True:
    print('Waiting for connection')
    client, address = server.accept()
    print('Connected from: ', address)
    handler = client_handler(client)
    handler.start()
    