
year = int(input('Give a year: '))

deelbaar_door_4 = year % 4 == 0
deelbaar_door_100 = year % 100 == 0
deelbaar_door_400 = year % 400 == 0
is_leapyear = deelbaar_door_4 and not deelbaar_door_100 or deelbaar_door_400



is_leapyear = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

print(year, is_leapyear)












if is_leapyear:
    print(f'{year} is a leapyear')
else:
    print(f'{year} is NOT a leapyear')
