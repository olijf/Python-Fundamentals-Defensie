import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

total = dice1 + dice2 + dice3 + dice4 + dice5

print('Thrown', dice1, dice2, dice3, dice4, dice5)
print('Total', total)



dices=[]
for _ in range(100):
    dices.append(random.randint(1,6))

print(dices)

print('Total', sum(dices))




dices = [random.randint(1,6) for _ in range(100)]

print('Thrown', dices)
print('Total', sum(dices))
