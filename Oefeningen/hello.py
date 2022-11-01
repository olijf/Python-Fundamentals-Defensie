"""
Dit is documentatie. In een docstring. Wordt door Python gebruikt met de help functie.
"""

# Dit is de input function
naam = input('Wat is jouw naam? ')

print('Hallo', naam)
print('Hallo ' + naam)

leeftijd = int(input('Hoe oud ben je? '))

print('Je bent dus', leeftijd)
print('Volgend jaar wordt je dus', leeftijd + 1)



print( naam + ' is ' + str(leeftijd) + ' years old' )
print( '%s is %d years old.' % (naam, leeftijd))
print( f'{naam} is {leeftijd} years old.' )



# print( name + ' is ' + str(age) + ' years old' )
# print( '%s is %d years old ' % (name, age) )
# print( '{} is {} years old'.format(name, age) )
# print( f'{name} is {age} years old' )
