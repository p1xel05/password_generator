import random as rnd
import string

alphabet = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

password = ""

for i in range(10):
    password += rnd.choice(alphabet)

for i in range(2):
    password += rnd.choice(numbers)

for i in range(1):
    password += rnd.choice(punctuation)

print(password)
