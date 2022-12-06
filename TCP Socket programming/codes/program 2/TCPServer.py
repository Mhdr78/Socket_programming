from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Client connected from ", addr)
    while True:
        sentence = connectionSocket.recv(1024)
        if not sentence or sentence.decode('utf-8') == 'END':
            break
        try:
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence)
        except:
            print('Exited by the user')
    connectionSocket.close()