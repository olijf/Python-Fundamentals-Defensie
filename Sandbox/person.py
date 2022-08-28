class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'My name is {self.name} and I live in {self.residence}')

    def move(self, new_residence):
        self.residence = new_residence
