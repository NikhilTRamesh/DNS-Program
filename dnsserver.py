#Nikhil Ramesh
#31499350
#Section 02
#! /usr/bin/env python3
# DNS Server
import sys
import socket
import time
import struct
import random

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
filepath = 'C:\CS356\DNS Program\dns-master.txt'
file = open(filepath,'r')
lines = file.readlines()
file.close()
# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")

# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    unpacked = struct.unpack('>iiiii32s', data)
    print("Received data from client " + address[0] + ", " + str(address[1]))
    messageID = unpacked[2]
    stringlength = unpacked[3]
    qstring = unpacked[5]
    returncode = 1
    answer = ''
    for line in lines:
        line2 = line[0:stringlength]
        if line2 in str(qstring):
            returncode = 0
            answer = line
            
    #dataEcho = struct.pack('>iiiii32s',2,returncode,messageID,stringlength,len(answer),answer.encode())
    print(returncode)
    print(answer)
    dataEcho = struct.pack('>ii64s',returncode,len(answer),answer.encode())
    # Echo back to client
    #data = struct.pack('!iiiiis',2,unpacked[1])
    print("Sending data to   client " + address[0] + ", " + str(address[1]))
    serverSocket.sendto(dataEcho,address)
