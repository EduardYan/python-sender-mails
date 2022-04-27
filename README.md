# Sender Mails Python.

This is a small program made with python for send mails quickly. With
a fast configuration.

## Installation.

```bash
$ git clone https://github.com/EduardYan/python-sender-mails.git

$ cd python-sender-mails

$ pip3 install -r ./requirements.txt
```

## Configuration.

Create a file called ".env" here set the following variables:

```env
# Info to send
MAIL_DESTINATARY = destinaryexample@gmail.com
MAIL_DIRECTION = myemailexample@gmail.com
MAIL_PASSWORD = mypasswordexample
```

## Running.

Only execute with:

```bash
$ python3 main.py
```