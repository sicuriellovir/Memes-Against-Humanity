import socket
import select
import random

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind((IP, PORT))
server_socket.listen(3)

socket_list = [server_socket]

clients = {}

def isReadyToStart():
	if count == 3:
		return True
	return False

readyToJudge = False
def isReadyToJudge():
	global readyToJudge
	if not readyToJudge:
		if judgeReadyCount == 3:
			readyToJudge = True
			return True
		else:
			return False
	else:
		if judgeReadyCount == 1:
			readyToJudge = False
		return True

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

def setCurrentMeme():
	global currentMemeFileName
	r = random.randint(1, 10)
	currentMemeFileName = "Meme" + str(r) + ".png"

def sendPhrase(client_socket):
	r = random.randint(1,30)
	file = "TestPhrase" + str(r)
	client_socket.send(file.encode())

def setNewJudge():
	global judgeClientNum
	global judgeClientSock

	judgeClientNum = (judgeClientNum + 1) % 3

	i = 0
	for client_sock in clients:
		if i == judgeClientNum:
			judgeClientSock = client_sock
		i += 1

count = 0
judgeClientNum = None
judgeClientSock = None
judgeReadyCount = 0
currentMemeFileName = None
setCurrentMeme()
selectedPhrases = {}
points = {}
readyForNewRound = False
notifiedOfNewRoundCount = 0
gameOver = False
SCORETOWIN = 5

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
				count -= 1
				continue

			user = clients[notified_socket]

			#the code below this line handles mechanics
			if message["data"].decode() == "IsServerReadyToStart":
				for client_socket in clients:
					if client_socket == notified_socket:
						if isReadyToStart():
							if judgeClientNum == None:
								judgeClientNum = 0
								judgeClientSock = client_socket
							client_socket.send("True".encode("utf-8"))
							username = clients[client_socket]["data"].decode()
							points[username] = 0
						else:
							client_socket.send("False".encode("utf-8"))

			elif message["data"].decode() == "ReadyForJudge":
				for client_socket in clients:
					if client_socket == notified_socket:
						judgeReadyCount += 1
						client_socket.send("True".encode("utf-8"))

			elif message["data"].decode() == "IsServerReadyToJudge":
				for client_socket in clients:
					if client_socket == notified_socket:
						if isReadyToJudge():
							client_socket.send("True".encode("utf-8"))
							judgeReadyCount -= 1
						else:
							client_socket.send("False".encode("utf-8"))

			elif message["data"].decode() == "CheckIfJudge":
				for client_socket in clients:
					if client_socket == notified_socket:
						if client_socket == judgeClientSock:
							client_socket.send("True".encode("utf-8"))
						else:
							client_socket.send("False".encode("utf-8"))

			elif message["data"].decode() == "GetMeme":
				for client_socket in clients:
					if client_socket == notified_socket:
						client_socket.send(currentMemeFileName.encode("utf-8"))

			elif message["data"].decode() == "GetNewPhraseCard":
				for client_socket in clients:
					if client_socket == notified_socket:
						sendPhrase(client_socket)

			elif message["data"].decode() == "AddSelectedPhrase":
				for client_socket in clients:
					if client_socket == notified_socket:
						phrase = recieve_message(client_socket)["data"].decode()
						print("Received phrase " + phrase)
						username = clients[client_socket]["data"].decode()
						selectedPhrases[username] = phrase
						client_socket.send("True".encode("utf-8"))

			elif message["data"].decode() == "GetJudgingPhraseCards":
				for client_socket in clients:
					if client_socket == notified_socket:
						phrases = ""
						for user in selectedPhrases:
							phrases += str(user) + " " + selectedPhrases[user] + " "
						phrases = phrases[:-1]
						client_socket.send(phrases.encode("utf-8"))

			elif message["data"].decode() == "IsServerReadyForNewRound":
				for client_socket in clients:
					if client_socket == notified_socket:
						if readyForNewRound:
							client_socket.send("True".encode("utf-8"))
							if notifiedOfNewRoundCount == 1:
								readyForNewRound = False
								notifiedOfNewRoundCount = 0
							else:
								notifiedOfNewRoundCount = 1
						else:
							client_socket.send("False".encode("utf-8"))

			elif message["data"].decode() == "SendRoundWinner":
				for client_socket in clients:
					if client_socket == notified_socket:
						roundWinnerName = recieve_message(client_socket)["data"].decode()
						points[roundWinnerName] += 1
						if points[roundWinnerName] == SCORETOWIN:
							gameOver = True
							client_socket.send("False".encode("utf-8"))
						else:
							client_socket.send("True".encode("utf-8"))

						#prepares for next round
						setNewJudge()
						selectedPhrases = {}
						setCurrentMeme()
						readyForNewRound = True

			elif message["data"].decode() == "GetPoints":
				for client_socket in clients:
					if client_socket == notified_socket:
						playerName = recieve_message(client_socket)["data"].decode()
						score = str(points[playerName])
						client_socket.send(score.encode("utf-8"))

			elif message["data"].decode() == "IsGameOver":
				for client_socket in clients:
					if client_socket == notified_socket:
						if gameOver:
							client_socket.send("True".encode("utf-8"))
						else:
							client_socket.send("False".encode("utf-8"))
