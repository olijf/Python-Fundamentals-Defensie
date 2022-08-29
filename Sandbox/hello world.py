import math

def my_func():
    """Dit is documnetatie van mijn hello world script
    @Copywrite Peter
    2022
    """
    print('Hoi')

voornaam = input('Wat is jouw voornaam? ')
achternaam = input('Wat is jouw achternaam? ')
leeftijd = int(input('Hoe oud ben je? '))

# concatenate de namen
naam = voornaam + ' ' + achternaam

print('Ik ben nogsteeds ' + naam)
print('Volgend jaar ben ben je dus ', leeftijd + 1)
