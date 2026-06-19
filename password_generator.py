import random as rnd
import string

alphabet = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(10):
    password += rnd.choice(alphabet)


print(password)