from socket import *

# initialize ip address and port number of server socket
serverPort = 12000
serverName = '127.0.0.1'

# create a tcp client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# start a three-way handshake with server
clientSocket.connect((serverName, serverPort))

# get a sentence from user
sentence = raw_input("Input lowercase sentence: ")

# send data to the server via tcp connection
clientSocket.send(bytes(sentence))

# receive response from server
modifiedSentence = clientSocket.recv(1024)

# show the response
print(modifiedSentence)

# close client socket connection with the server
clientSocket.close()
