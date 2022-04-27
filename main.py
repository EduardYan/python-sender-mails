#!/usr/bin/env python3
"""
Script for practice how
send emails.

Important !
Allow the permissions for recived the email, visit this direction:
https://myaccount.google.com/lesssecureapps


"""

import smtplib
import socket
from decouple import config
from mail import Mail
from colorama import Back, Fore, init


def main():
  """
  Principal function to execute.
  """

  # Info of the mail
  MAIL_DESTINATARY = config('MAIL_DESTINATARY')
  MAIL_DIRECTION = config('MAIL_DIRECTION')
  MAIL_PASSWORD = config("MAIL_PASSWORD")


  # Getting Data
  with open('./data/message.txt', 'r') as f:
    message = f.read()
    f.close()

  subject = "Testing of Mail"

  # Message with the subject
  message = f"Subject: {subject}\n\n{message}"

  # Creating the mail, first the
  mail = Mail(MAIL_DESTINATARY, MAIL_DIRECTION, message)

  try:
    # Server and port
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login with our email
    server.login(MAIL_DIRECTION, MAIL_PASSWORD)

    # The first is what send the email and the second is who recived
    server.sendmail(mail.remitent, mail.destinatary, mail.message)

    server.quit()

    print(Back.BLACK + Fore.LIGHTGREEN_EX + f"Mail send successfully from {MAIL_DIRECTION} to {MAIL_DESTINATARY}")

  # Erros Control
  except socket.gaierror:
    print(Back.BLACK + Fore.RED + "The network is unstable. Verify the network !")
  
  except smtplib.SMTPAuthenticationError:
    print(Back.BLACK + Fore.RED + "Username or Password not accepted !")

  except smtplib.SMTPServerDisconnected:
    print(Back.BLACK + Fore.RED + "The is server disconnected !")

  except smtplib.SMTPConnectError:
    print(Back.BLACK + Fore.RED + "Error to connect with the server !")


if __name__ == '__main__':
  # Autoreset for colorama colors
  init(autoreset = True)

  print('\n')
  main()
  print('\n')