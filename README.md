# DNS-Program

Python Server-Client approach to a simplified Domain Name System

Client performs three main functions:

Read IP address of server, Port of server, hostname from command line

Send a request containing specified hostanem in header format

Wait for response from server using timeout socket protocols

Server performs the following functions:

Reads in IP address of server and Port of server via command line

Reads in master file name: E.G. dns-master.txt in this case to check domain names

Stores resource records of TYPE A domains from dns-master.txt for searching

Responds to requests from DNS client and returns the appropriate message format
