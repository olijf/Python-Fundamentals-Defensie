

class Club:
    pass

class Team:
    def __init__(self):
        self.spelers = []

    def speler_toevoegen(self, speler):
        self.spelers.append(speler)

class Speler:
    def __init__(self, naam, rugnummer, positie):
        self.naam = naam
        self.rugnummer = rugnummer
        self.positie = positie

class Wedstrijd:
    pass

#----------------------------------------