"""
Envia um e-mail com uma lista dos melhores filmes de todos os tempos da url
http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/
"""

import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail(message):
    HOST = "smtp.gmail.com"
    PORT = 587
    USER = os.getenv("MAIL_FROM")
    PASSWORD = os.getenv("PASSWORD")
    TO = os.getenv("MAIL_TO")

    server = smtplib.SMTP(HOST, PORT)
    server.ehlo()
    server.starttls()
    server.login(USER, PASSWORD)

    email_msg = MIMEMultipart()
    email_msg["From"] = USER
    email_msg["To"] = TO
    email_msg["Subject"] = "teste de envio de email"
    email_msg.attach(MIMEText(message, "html"))

    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    server.quit()
