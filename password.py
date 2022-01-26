#random safe passwordmaker

import secrets
import string
alphabet = string.printable #all printable ASCII characters.
password = ''.join(secrets.choice(alphabet) for i in range(10)) #you can adjust the length of the password here in range() method
password
