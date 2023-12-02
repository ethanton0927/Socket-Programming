#Ethan Ton
import os
import struct
import sys
from socket import*



#Get Function
def get(fileName):
    clientSocket.send("get".encode())
    print(fileName)
    
#Upload Function
def put(fileName):
    #Send command to Server
    clientSocket.send("put".encode())
    
    #Open the file to be able to read contents
    data = open(fileName, "rb")
    
    clientSocket.send(struct.pack("h", sys.getsizeof(fileName)))
    clientSocket.send(fileName)
    
    clientSocket.send(struct.pack("i", os.path.getsize(fileName)))
    
    dataSend = data.read(40)
    
    while dataSend:
        clientSocket.send(dataSend)
        dataSend = data.read(40)
#List Function
def list():
    #Sends the list command to the Server
    clientSocket.send("list".encode())
    
    #Retrieves from server the number of items to be listed
    numItems = clientSocket.recv(40).decode()
    
    #List to contain the data retrieved
    listPrint = []
    
    #For loop receives data from the server and appends to list
    for x in range(int(numItems)):
        data = clientSocket.recv(1024)
        listPrint.append(data.decode())

    #For loop prints the list of files
    for x in listPrint:
        print(x)
        
#Quit Function
def quit():
    clientSocket.send("quit".encode())
    print("Disconnecting from server")
    clientSocket.close()
    print("Closing program")
    exit()
    
#Main =========================================================================

#Receive Domain and Port
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

#Create Socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#Connect to server
clientSocket.connect((serverName, serverPort))

#Main Input Loop
while True:
    #Prompt User for their input
    print("FTP> ", end="")
    
    #Receive User Input
    userInput = input()

    #Check User Input against list of commands
    if(userInput[:3] == "get"):
        get(userInput[4:])
    elif(userInput[:3] == "put"):
        put(userInput[4:])
    elif(userInput[:2] == "ls"):
        list()
    elif(userInput[:4] == "quit"):
        quit()
    else:
        print("Please enter a proper command")