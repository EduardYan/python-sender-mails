"""
Model for a mail.
"""


class Mail:
    """

    Model for a mail, with properties
    remitent
    destinatary
    message
    """

    def __init__(self, remitent: str, destinatary: str, message: str = 'Test') -> None:
        self.remitent = remitent
        self.destinatary = destinatary
        self.message = message