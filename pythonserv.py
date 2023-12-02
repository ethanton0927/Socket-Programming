#Ethan Ton
import os
from socket import*
import struct
import sys

#Get Function
def get():
    print("f")

#Put Function
def put():
    print("f")

#List Function
def list():
    print("Listing files")
    
    #Collect list of files from directory
    listDir = os.listdir()
    connectionSocket.send(str(len(listDir)).encode())
    
    for i in listDir:
        print(i)
        connectionSocket.send(i.encode("utf-8"))
        

#Quit Function
def quit():
    print("Closing connection")
    connectionSocket.close()
    print("Disconnecing socket")
    serverSocket.close
    print("Closing server")
    exit()
    #Disconnect from 


#Main =========================================================================

#Server Port
serverPort = 12000

#Create TCP Socket
serverSocket = socket(AF_INET,SOCK_STREAM)

#Bind the Socket to Port
serverSocket.bind(('', serverPort))
print("Binding Port")

#Start listening for incoming connections
serverSocket.listen(1)
print("Listening for connections")

#Accept Connection
connectionSocket, address = serverSocket.accept()

data = ""
while True:
    print("Waiting for instructions")
    data = connectionSocket.recv(40)
    
    if(data.decode() == "get"):
        get()
    elif(data.decode() == "put"):
        put()
    elif(data.decode() == "list"):
        list()
    elif(data.decode() == "quit"):
        quit()
    data = None