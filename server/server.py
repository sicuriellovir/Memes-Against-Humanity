import threading
import socket
import select
import os
import random

host = '127.0.0.1'
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients = [] #list of clients
usernames = []

def isReady():
	if count == 3:
		return True

count=0
print(f'Listening for connections on {host}:{port}...')
while True:
	client, address = server.accept()
	count+=1
	print(f"Connected with {str(address)}")		
	username = client.recv(1024).decode('ascii')
	usernames.append(username)
	clients.append(client)
	print(f'Username: {username}')
	mRandom = random.randint(1,7)
	meme = f"testMeme{str(mRandom)}"
	client.send(f'{meme}'.encode(('utf-8')))
	pRandom = random.randint(1,31)
	phrases = f"TestPhrase{str(pRandom)}"
	client.send(f'{phrases}'.encode(('utf-8')))
		
