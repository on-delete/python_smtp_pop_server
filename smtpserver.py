import smtpd
import asyncore
import os.path
import time

class CustomSMTPServer(smtpd.SMTPServer):
    
    print("Server gestartet!")

    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        
        #Schleife fuer alle Empfaenger, die die email erhalten
	for val in rcpttos:

		#Falls der Ordner fuer den Empfaenger noch nicht angelegt ist, wird
		#dies getan.
		if not os.path.exists(val):
			os.mkdir(val)
			
		#datei bekommt aktuellen Zeitstempel als Namen	
		filename = time.strftime("%d.%m.%Y %H:%M:%S").replace(' ', '')		

		print 'LOG: Email wird in Datei ' + filename + ' gespeichert.'		
 
 		#datei wird geoeffnet, beschrieben mit der Email und geschlossen
		path = val + "/" + filename
		d = open(path, "w")
		d.write(data)
		d.close

		print 'LOG: Email erfolgreich abgespeichert.'
	
	return

server = CustomSMTPServer(('0.0.0.0', 8888), None)

#Der Server laueft in einer Schleife, damit er immer neue Emails empfangen kann.
asyncore.loop()
