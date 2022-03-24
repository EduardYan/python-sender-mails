"""
Script for practice how
send emails.
"""

import smtplib
from decouple import config
from mail import Mail


# Data
message = "Hello, this is a message for make a test with python"
subject = "Testing of Mail"

# Message with the subject
message = f"Subject: {subject}\n\n{message}"

mail = Mail("eduarygp@gmail.com", "eduarygp@gmail.com", message)

# Server and port
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login with our email
server.login("eduarygp@gmail.com", config("MAIL_PASSWORD"))

# The first is what send the email and the second is who recived
server.sendmail(mail.remitent, mail.destinatary, mail.message)

server.quit()

print("Mail send successfully")
