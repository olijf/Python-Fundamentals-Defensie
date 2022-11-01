filename_in = 'addresses.txt'
filename_out = 'addresses_filtered.txt'

with open(filename_in) as f_in:
    with open(filename_out, 'w') as f_out:
        for line in f_in:
            line = line.rstrip('\n')
            if '@' in line:
                print(line)
                print(line.upper(), file = f_out)