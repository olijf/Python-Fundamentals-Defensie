names = []

while True:
    name = input('Enter a name: ')

    if not name:
        break

    names.append(name)

for name in sorted(names):
    print(name)
