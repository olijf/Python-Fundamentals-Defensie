class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        return (f'I am {self.name} from {self.residence}')

    def move(self, new_residence):
        self.residence = new_residence


# ------------------------------------------------------------

p1 = Person('Albert', 'Amsterdam')
print(p1.tell())
p1.move('Urk')
print(p1.tell())

p2 = Person('Gert Jan', 'Den Haag')
print(p2.tell())

p3 = Person('Gert Jan', 'Den Haag')
print(p3.tell())