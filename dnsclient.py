#Nikhil Ramesh
#31499350
#Section 02
#! /usr/bin/env python3
# DNS Client
import sys
import socket
import time
import struct
import random

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
hostname = sys.argv[3]
messagetype = 1
returncode = 0
messageID = random.randint(0,100)
qstring = hostname + " A IN"
qlength = len(qstring)
# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to server
data = struct.pack('>iiiii32s',1,0,messageID,qlength,0,qstring.encode())
print("Sending request to " + host + ", " + str(port))
print("Message ID: " + str(messageID))
print("Question Length: " + str(qlength) + " bytes")
print("Answer Length: 0 bytes")
print("Question: " + qstring)
print("")

clientsocket.sendto(data,(host, port))
clientsocket.settimeout(1)
count = 0

#Receive the server response
while count < 3:
    try:
        dataEcho, address = clientsocket.recvfrom(1024)
        break
    except socket.error:
        count = count + 1
        print("Sending request to " + host + ", " + str(port))
        print("Request timed out ...")
if count == 3:
    print("Exiting program")
    quit()
#print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
if (count < 3):
    unpacked = struct.unpack('>ii64s',dataEcho)
    s = qstring
    rcode = unpacked[0]
    mid = messageID
    slength = qlength
    alength = unpacked[1]
    a = unpacked[2].decode()
    rprint = "Return Code: " + str(rcode)
    if (rcode == 0):
        rprint = rprint + " (No errors)"
    else:
        rprint = rprint + " (Name does not exist)"
    print("Received Response from " +host + ", " + str(port) + ":")
    print(rprint)
    print("Message ID: " + str(mid))
    print("Question Length: " + str(slength) + " bytes")
    print("Answer Length: " + str(alength) + " bytes")
    print("Question: " + s)
    if alength > 0:
        print("Answer: " + a)
    #Close the client socket
clientsocket.close()
