from socket import *
serverPort = 12000
serverName = '127.0.0.1'
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input lowercase sentence:")
try:
    while True:
        clientSocket.send(sentence.encode('utf-8'))
        modifiedSentence = clientSocket.recv(1024).decode('utf-8')
        print(modifiedSentence)
        more = input("Want to send more data to Server?")
        if more.lower() =='y':
            sentence = input("Input lowercase sentence:")
        else:
            break
except KeyboardInterrupt:
    print("Exited by the user")
clientSocket.close()
