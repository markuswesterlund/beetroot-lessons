"""
Create a class method named `validate`, which should be called from
the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method
could be to check if the passed email parameter is a valid email string.
"""

import re


class Checkmail:

    def __init__(self, email):
        self.email = email

    @classmethod
    def validate(cls, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return f"{email} is a valid e-mail address"
        else:
            return f"{email} is not a valid e-mail address"


mail1 = Checkmail.validate("westerlund@hotmail.se")
mail2 = Checkmail.validate("westerlundhotmailse")
mail3 = Checkmail.validate("@markus.com_markus")

print(mail1)
print(mail2)
print(mail3)
