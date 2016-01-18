import socket
import sys
from thread import *
import os
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8889 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'POP3 Server gestartet!'
 
#Start listening on socket
s.listen(10)
#print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    #conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024).decode()
	answer = data.split( )
	
	action = answer[0]
	email = answer[1]

	file_entries = os.listdir(email)
	
        if action=='LIST':
		#print 'Anzahl emails im ordner: ', len(file_entries)
		print "Anzahl emails wird abgerufen fuer: ", email
		retmessage = '+OK '+ str(len(file_entries))
		conn.sendall(retmessage)
	elif action=='RETR':
		print "email wird abgerufen fuer: ", email 
		n = answer[2]
		for var in file_entries:
			file = open(email +"/"+ var, "r")
			content = file.read()
			#print content
			
			conn.sendall("+OK " + content)
	else:
		conn.sendall("Keine gueltige Operation!")
     
    #came out of loop
    #conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    #print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
