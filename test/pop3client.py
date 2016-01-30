import socket
import sys

if len(sys.argv) < 2:
	print "Der Befehl muss wie folgt aufgerufen werden: pop3client.py mail@example.de"
	sys.exit(2)

email_address  = sys.argv[1]

server_address = "192.168.2.122"
port = 8889

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = (server_address, port)

sock.connect(server)

message = "LIST " + email_address
sock.sendall(message)
print "Anfrage an POP3 gestellt \n"
    
data = sock.recv(1024)
antwort = data.split( )

if antwort[0]=='+OK':
	print "Anzahl Nachrichten: ", antwort[1]

	for i in range(int(antwort[1])):
		message = 'RETR ' + email_address + ' ' + str(i)
		sock.sendall(message)
		print "\n email wird abgerufen... \n"
		
		data = sock.recv(1024)
		code = data[:4]
		email = data[4:]
		#print code
		print "Nachricht :\n", email  

else:
	print data
sock.close()
