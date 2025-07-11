import smtplib
from email.message import EmailMessage
import os

def send_email(to, subject, body):
    sender = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASS')

    if not sender or not password:
        raise ValueError("Email credentials not set")

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
