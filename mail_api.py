import smtplib
import sys
from email.mime.text import MIMEText

import preferences as prefs

EMAIL_ADDRESS = 'outstanding@estsoft.com'

def send_mail(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('outstanding@estsoft.com', prefs.GOOGLE_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
    server.close()
