# Password Generator

import random
import string

length = 12

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range (length))

print("Generated Password:", password)