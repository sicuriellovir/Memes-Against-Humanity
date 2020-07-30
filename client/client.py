import socket
import errno
import sys
from .Card import PhraseCard, MemeCard

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))

def Connect(my_username):
	while True:
		try:
			client.send(my_username.encode('utf-8'))
			meme = client.recv(1024).decode('utf-8')
			phrase = client.recv(1024).decode('utf-8')
			print(phrase)
			print(meme)
			mCard = MemeCard(meme)
			pCard = PhraseCard(phrase, my_username)
		except IOError as e:
			if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
				print('Reading error: {}'.format(str(e)))
				sys.exit()
			continue
		except:
			print("ERROR")
			client.close()
			break
