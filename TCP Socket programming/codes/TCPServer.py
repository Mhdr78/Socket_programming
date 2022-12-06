from socket import *

# initialize ip address and port number of server socket
serverPort = 12000

# create a tcp server socket e.g, welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind the port 12000 to the serverSocket
serverSocket.bind(('', serverPort))

# get ready for listening to the clients
serverSocket.listen(1)

print("the server is ready to receive\n")

# server stays in infinite loop to receive
while True:
    print "... waiting for requests ..."
    # create new connectionSocket per each client connect requests and save their addresses too.
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print "Client connected from %s:%s" % (ip, port)

    # get data from client
    sentence = connectionSocket.recv(1024)
    print "received from client: %s\n" % sentence

    # change the data to the uppercase.
    capitalizedSentence = sentence.upper()

    # send response to the client via tcp connection
    connectionSocket.send(bytes(capitalizedSentence))
    # then close the connection socket at the end.
    connectionSocket.close()
