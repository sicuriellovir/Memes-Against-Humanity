import socket
import select
import errno
import sys
from .Card import PhraseCard, MemeCard

def Connect(my_username):
	HEADER_LENGTH = 10

	IP = "127.0.0.1"
	PORT = 1234

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((IP,PORT))
	username = my_username.encode('utf-8')
	username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
	client_socket.send(username_header + username)

	while True:
		try:
			while True:
				meme_header = client_socket.recv(1024)
				if not len(meme_header):
					print("Connection closed by the server")
					sys.exit()				
				meme_length = int(meme_header.decode('utf-8').strip())
				meme = client_socket.recv(meme_length).decode('utf-8')
				phrase_header = client_socket.recv(HEADER_LENGTH)
				phrase_length = int(phrase_header.decode('utf-8').strip())
				phrase = client_socket.recv(phrase_length).decode('utf-8')		
				pCard = server.PhraseCard(phrase, my_username)
				mCard = server.MemeCard(meme)

		except IOError as e:
			if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
				print('Reading error: {}'.format(str(e)))
				sys.exit()
			continue

		except Exception as e:
			print('General error: '.format(str(e)))
			sys.exit()
