

class Person:

    __slots__ = ['_name', '_residence']

    def __init__(self, name, residence):
        self._name = name
        self._residence = residence

    def __str__(self):
        return self._name + ' from ' + self._residence

    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}.')


class Player(Person):
    
    def __init__(self, name, residence, number):
        super().__init__(name, residence)
        self._number = number

    def tell(self):
        print(f'I am {self._name} with number {self._number} and I live in {self._residence}.')

        
class Trainer(Person):
    
    def __init__(self, name, wears_a_suit = False):
        super().__init__(name, 'not relavent')
        self._wears_a_suit = wears_a_suit

    def tell(self):
        print(f'I am {self._name} and I am the trainer.')
        if self._wears_a_suit:
            print('I always wear a suit')
        else:
            print('I never wear a suit')
            




#=================================

if  __name__ == '__main__':

    p1 = Person('Peter', 'Lhee')
    p1.tell()

    p2 = Person('Kazuko', 'Eindhoven')
    p2.tell()

    print(str(p1))
    print(str(p2))

    team = []
    team.append( Player('Peter', 'Lhee', '5') )
    team.append( Player('Roman', 'Eindhoven', '2') )
    team.append( Player('Jaap', 'Eindhoven', '9') )
    team.append( Player('Wojeck', 'Eindhoven', '11') )
    team.append( Player('Joao', 'Veldhoven', '14') )

    for player in team:
        player.tell()

    trainer = Trainer('Frank', wears_a_suit = True)

    trainer.tell()

    
