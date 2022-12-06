from socket import *
from time import ctime

# initialize ip and port number of server
HOST = "127.0.0.1"
PORT = 12000
BUFSIZE = 1024
ADDR = (HOST, PORT)

# create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# you can exit from this loop by typing "exit"
# and you should enter an simple expression
# e.g., 2 + 3, 7 * 5, 10 / 2, 4 - 6
while True:
    sendData = raw_input(">> ")
    if sendData.lower() == "exit":
        break
    if sendData is None:
        break
    # send message to server
    clientSocket.sendto(sendData, ADDR)

    print "...waiting for response..."

    # receive response from server include expression answer
    recv_data, ADDR = clientSocket.recvfrom(BUFSIZE)

    # show the response
    if recv_data != "":
        print "[%s]: received data from server %s:%s : %s" % (ctime(), ADDR[0], ADDR[1], recv_data)

clientSocket.close()