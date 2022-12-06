from socket import *
from time import ctime

# initialize ip and port number of server
HOST = ''
PORT = 12000
BUFSIZE = 1024
ADDR = (HOST, PORT)

# create UDP server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind (ip,port) to serverSocket
serverSocket.bind(ADDR)

# now ready to receive messages
while True:
    print "...waiting for message..."

    # receive data from client
    data, ADDR = serverSocket.recvfrom(BUFSIZE)
    if data is None:
        break
    # show pure data
    print "[%s]: From Address %s:%s received data: %s" % (ctime(), ADDR[0], ADDR[1], data)

    # Calculate result
    # split operands and operation symbol
    expr = data.split(" ")
    num1 = float(expr[0])
    num2 = float(expr[-1])
    opr = expr[1]
    res = "not valid! try again"
    # recognize which operation i.e., +, -, *, /
    if opr == "+":
        res = num1 + num2
    elif opr == "-":
        res = num1 - num2
    elif opr == "*":
        res = num1 * num2
    else:
        res = num1 / num2

    # show response with time
    print "[%s]: Server Response: %s" % (ctime(), res)

    # send response to client
    if res is not None:
        serverSocket.sendto(bytes(res), ADDR)

serverSocket.close()

