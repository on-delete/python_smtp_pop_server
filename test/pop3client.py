import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.10.0.154', 8889)
#print "connecting to port 8889"
sock.connect(server_address)

message = "LIST pi@gmail.com"
sock.sendall(message)
print "Anfrage an POP3 gestellt \n"
    
data = sock.recv(1024)
antwort = data.split( )


if antwort[0]=='+OK':
	print "Anzahl Nachrichten im Ordner: ", antwort[1]

	for i in range(int(antwort[1])):
		message = 'RETR pi@gmail.com ' + str(i)
		sock.sendall(message)
		print "\n email wird abgerufen... \n"
		
		data = sock.recv(1024)
		code = data[:4]
		email = data[4:]
		#print code
		print "Nachricht :\n", email  
	
sock.close()
