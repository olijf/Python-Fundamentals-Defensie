filename = '../Sandbox/ca-500.csv'

with open(filename, 'r') as f:
    headers = f.readline().strip().split(';')

    for line in f:
        values = line.strip().split(';')

        d = dict(zip(headers, values))

        if d['city'] in ('Montreal', 'Vancouver'):
            print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")
