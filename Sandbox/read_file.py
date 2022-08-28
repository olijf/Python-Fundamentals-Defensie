import re

filename = 'ca-500.csv'

with open(filename, 'r') as f:
    headers = f.readline().strip().split(';')

    for line in f:
        values = line.strip().split(';')

        d = dict(zip(headers, values))

        if d['city'] in ('Montreal',):

            print('%-15s %-15s %-35s %-25s' %
                  (d['first_name'], d['last_name'], d['email'], d['city']))

