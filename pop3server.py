import socket
import sys
from thread import *
import os

HOST = ''
PORT = 8889

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'POP3 Server gestartet!'

s.listen(10)

#Funktion fuer den Thread, die alle ankommenden Nachrichten behandelt
def clientthread(conn):
    while True:

        #Nachricht von Client
        data = conn.recv(1024).decode()
        answer = data.split( )

        action = answer[0]
        email = answer[1]

        #Falls die email adresse bekannt ist, wird je nach Aktion "LIST" oder "RETR" die Anzahl der
        #emails oder die emails selbst an den Cliet zurueckgeschickt.
        if os.path.exists(email):
                file_entries = os.listdir(email)

                if action=='LIST':
                        retmessage = '+OK '+ str(len(file_entries))
                        conn.sendall(retmessage)
                elif action=='RETR':
                        n = answer[2]
                        for var in file_entries:
                                file = open(email +"/"+ var, "r")
                                content = file.read()

                                conn.sendall("+OK " + content)
                else:
                        conn.sendall("Keine gueltige Operation!")

        else:
                conn.sendall("+FAIL Emailadresse ist nicht bekannt")

#In der While Schleife wird immer auf eine Connection gewartet. Sobald diese erfolgt, wird die
#Funktion in einem neuen Thread ausgefuehrt
while 1:
    conn, addr = s.accept()
    
    start_new_thread(clientthread ,(conn,))

s.close()
