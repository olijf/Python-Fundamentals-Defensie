#!/usr/bin/python
import random
import string

password = []
options = ['lower', 'upper', 'number', 'char']

def give_lower():
    return random.choice(string.ascii_lowercase)

def give_upper():
    return random.choice(string.ascii_uppercase)

def give_number():
    return random.choice(string.digits)

def give_char():
    return random.choice(string.punctuation)

while True:
    length = int(input("Voer de lengte in: "))
    if 8 <= length <= 20:
        break
    if 0 <= length <= 8:
        print("unsafe password length, to short")
    else:
        print("Password too long, impossible to remember")

password.extend([give_lower(), give_upper(), give_number(), give_char()])

# Substract the required lower, upper, number and char
length = length - 4

for _ in range(length):
    pick = random.choice(options)
    if pick == "lower":
        password.append(give_lower())
    if pick == "upper":
        password.append(give_upper())
    if pick == "number":
        password.append(give_number())
    if pick == "char":
        password.append(give_char())

random.shuffle(password)
password = ''.join(password)

print(password)