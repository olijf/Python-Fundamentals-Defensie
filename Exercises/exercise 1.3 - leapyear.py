
year = int(input('Give a year: '))

is_leapyear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(year, is_leapyear)

if is_leapyear:
    print(f'{year} is a leapyear')
else:
    print(f'{year} is not a leapyear')
