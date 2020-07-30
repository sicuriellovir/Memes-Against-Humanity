import socket
from .GUI import GUIhandler as GUI
import select
from time import sleep
import errno
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HEADER_LENGTH = 10
def Connect(my_username):
	global client_socket

	IP = "127.0.0.1"
	PORT = 1234

	client_socket.connect((IP,PORT))
	client_socket.setblocking(False)

	username = my_username.encode('utf-8')
	username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
	client_socket.send(username_header + username)

def checkIfReadyToStart():
	return sendToServer(["IsServerReadyToStart"])

def setAsReadyForJudge():
	return sendToServer(["ReadyForJudge"])

def checkIfReadyToJudge():
	return sendToServer(["IsServerReadyToJudge"])

def checkIfJudge():
	return sendToServer(["CheckIfJudge"])

def getCurrentMeme():
	return sendToServer(["GetMeme"])

def getNewPhraseCard():
	return sendToServer(["GetNewPhraseCard"])

def isJudge():
	return sendToServer(["CheckIfJudge"])

def sendSelectedPhraseCard(phraseFileName):
	return sendToServer(["AddSelectedPhrase", phraseFileName])

def getJudgingPhraseCards():
	return sendToServer(["GetJudgingPhraseCards"]).split()

def sendRoundWinner(roundWinnerName):
	return sendToServer(["SendRoundWinner", roundWinnerName])

def checkIfReadyForNewRound():
	return sendToServer(["IsServerReadyForNewRound"])

def getPoints(name):
	return sendToServer(["GetPoints", name])

def isGameOver():
	return sendToServer(["IsGameOver"])

def sendToServer(messages):
	for message in messages:
		if message:
			message = message.encode('utf-8')
			message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
			client_socket.send(message_header+message)

	try:
		sleep(0.3)
		message = client_socket.recv(1024).decode('utf-8')

		if message == "True":
			return True
		elif message == "False":
			return False
		else:
			return message

	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Reading error: {}'.format(str(e)))
			sys.exit()

	except Exception as e:
		print('General error: '.format(str(e)))
		sys.exit()