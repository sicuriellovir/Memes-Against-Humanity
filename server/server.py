import socket
import select
import random
import os

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()

socket_list = [server_socket]
clients = {}

def isReady():
	if count == 3:
		return True

def sendMeme(client_socket):
	folder = r"Memes-Against-Humanity/client/Card/memes"
	a = random.choice(os.listdir(folder))
	file = folder +'/'+a
	file = file.encode()
	return client_socket.send(file)

def sendPhrase(client_socket):
	r = random.randint(1,31)
	result = f"TestPhrase {str(r)}".encode()
	return client_socket.send(result)

print(f'Listening for connections on {IP}:{PORT}...')
def recieve_message(client_socket):
	try:
		message_header = client_socket.recv(HEADER_LENGTH)
		if not len(message_header):
			return False
		message_length = int(message_header.decode('utf-8').strip())
		return {'header': message_header, 'data': client_socket.recv(message_length)}
	except:
		return False

count=0
while True:
	read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)
	for notified_socket in read_sockets:
		if notified_socket == server_socket:
			client_socket, client_address = server_socket.accept()
			count += 1
			user = recieve_message(client_socket)
			if user is False:
				continue

			socket_list.append(client_socket)

			clients[client_socket] = user

			print('Accepted new connection from {}:{}, username:{}'.format(*client_address, user['data'].decode('utf-8')))

		else:
			message = recieve_message(notified_socket)

			if message is False:
				print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
				socket_list.remove(notified_socket)
				del clients[notified_socket]
				continue

			user = clients[notified_socket]

			print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
			for client_socket in clients:
				if client_socket != notified_socket:
					client_socket.send(user['header'] + user['data']+ message['header'] + message['data'])
					sendPhrase(client_socket)
					sendMeme(client_socket)

for notified_socket in exception_sockets:
	socket_list.remove(notified_socket)
	del clients[notified_socket]
