import smtplib
import email.utils
from email.mime.text import MIMEText
import sys
import ast

if len(sys.argv) < 5:
	print "Der Befehl muss wie folgt aufgerufen werden: client.py from@example.com \"['to@example.com', '...']\" betreff \"inhalt\""
	sys.exit(2)

from_mail = sys.argv[1]
to_mail = ast.literal_eval(sys.argv[2])
betreff = sys.argv[3]
inhalt = sys.argv[4]

msg = MIMEText(inhalt)
msg['From'] = email.utils.formataddr(('Author', from_mail))
msg['Subject'] = betreff

server = smtplib.SMTP('192.168.2.122', 8888)
try:
	server.sendmail(from_mail, to_mail, msg.as_string())
finally:
    server.quit()
