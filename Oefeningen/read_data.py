
filename = 'data.txt'

try:
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.endswith('processing'):
                print(line)

except FileNotFoundError:
    print(f'File {filename} bestaat niet.')