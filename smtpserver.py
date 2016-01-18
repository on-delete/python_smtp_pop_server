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
        #print 'Message length        :', len(data)
	#print 'Data		     :', data
        
	for val in rcpttos:

		if not os.path.exists(val):
			os.mkdir(val)
	
		filename = time.strftime("%d.%m.%Y %H:%M:%S").replace(' ', '')		


		print 'LOG: Email wird in Datei ' + filename + ' gespeichert.'		
 
		path = val + "/" + filename
		d = open(path, "w")
		d.write(data)
		d.close

		print 'LOG: Email erfolgreich abgespeichert.'
	
	return

server = CustomSMTPServer(('0.0.0.0', 8888), None)

asyncore.loop()
