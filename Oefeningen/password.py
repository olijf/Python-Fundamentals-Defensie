import random

upper = random.choices('ABCDEFGHJKLMNPQRSTUWVXYZ', k=2)    # exclude I, O
lower = random.choices('abcdefghijkmnopqrstuwvxyz', k=2)    # exclude l
number = random.choices('0123456789', k=1)
special = random.choices('!@#$%&', k=1)

all = upper + lower + number + special

random.shuffle(all)

password = ''.join(all)

print(password)