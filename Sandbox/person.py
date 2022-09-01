from datetime import date

class Person:

    def __init__(self, name, residence, geboortedatum = None):
        self.name = name
        self.residence = residence
        self.geboortedatum = geboortedatum

    def tell(self):
        leeftijd_text = f'Ik ben {self.leeftijd}.' if self.leeftijd else 'Leeftijd onbekend.'
        return (f'I am {self.name} from {self.residence}. {leeftijd_text}')

    def move(self, new_residence):
        self.residence = new_residence

    @property
    def leeftijd(self):
        if self.geboortedatum is not None:
            return int((date.today() - date.fromisoformat(self.geboortedatum)).days // 365.25)
        else:
            return None


# ------------------------------------------------------------

p1 = Person('Albert', 'Amsterdam')
print(p1.tell())
p1.move('Urk')
print(p1.tell())

p2 = Person('Gert Jan', 'Den Haag', '1999-02-25')
print(p2.tell())

p3 = Person('Gert Jan', 'Den Haag', '1958-02-28')
print(p3.tell())