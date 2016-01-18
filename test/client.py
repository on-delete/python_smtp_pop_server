import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('Heute schneit es!')
#msg['To'] = email.utils.formataddr(('Recipient', 'pi@gmail.com'))
msg['From'] = email.utils.formataddr(('Author', 'andre2@example.com'))
msg['Subject'] = 'Noch eine Nachricht'

server = smtplib.SMTP('0.0.0.0', 8888)
server.set_debuglevel(False) # show communication with the server
try:
    server.sendmail('author@example.com', ['pi@gmail.com', 'pi2@gmail.com'], msg.as_string())
finally:
    server.quit()
