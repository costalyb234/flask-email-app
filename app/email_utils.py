import smtplib
from email.message import EmailMessage
import os
import ssl

def send_email(subject, body):
    sender = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASS')
    sender_name = "God of Web"

    if not sender or not password:
        raise ValueError("Email credentials not set")

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = f"{sender_name} <{sender}>"
    msg['To'] = os.environ.get('EMAIL_TO')

    # Disable certificate verification (temporary workaround)
    context = ssl._create_unverified_context()

    with smtplib.SMTP('mail.bpserver.site', 587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)  # Pass the unverified context here
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.send_message(msg)
