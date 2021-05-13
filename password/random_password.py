import string
from random import choice
alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(choice(alphabet) for i in range(25))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 4):
        break
print(password)
