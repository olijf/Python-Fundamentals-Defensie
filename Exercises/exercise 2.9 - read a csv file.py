
filename = '../Sandbox/ca-500.csv'

with open(filename, 'r') as f:

    headers = f.readline().strip().split(';')

    for line in f:
        values = line.strip().split(';')

        d = dict(zip(headers, values))

        if d['city'] in ('Montreal', 'Toronto'):
            print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")







# import csv
#
# with open(filename, 'r') as f:
#     reader = csv.DictReader(f, delimiter=';')
#
#     for d in reader:
#
#         if d['city'] in ('Montreal', 'Toronto'):
#             print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")

import pandas as pd

df = pd.read_csv(filename, sep=';')

df_select = df[df['city']=='Montreal']

for line in df_select[['first_name','last_name','city']]:
    print(line)
