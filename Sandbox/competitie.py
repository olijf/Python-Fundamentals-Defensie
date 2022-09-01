import pickle

class Club:
    def __init__(self, naam, plaats):
        self.id = 675
        self.naam = naam
        self.plaats = plaats
        self.teams = []

    def team_toevoegen(self, team):
        self.teams.append(team)

    def store_in_pickle(self, filename = 'club.pickle'):
        with open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f)

    def restore_from_pickle(self, filename = 'club.pickle'):
        with open(filename, 'rb') as f:
            self.__dict__.update(pickle.load(f))


class Team:
    def __init__(self, naam):
        self.id = 23
        self.club_id = 675
        self.naam = naam
        self.spelers = []

    def speler_toevoegen(self, *spelers):
        for speler in spelers:
            self.spelers.append(speler)

class Speler:
    def __init__(self, naam, rugnummer, positie):
        self.naam = naam
        self.rugnummer = rugnummer
        self.positie = positie

class Wedstrijd:

    def __init__(self, datum, plaats, thuis_team, uit_team):
        self.datum = datum
        self.plaats = plaats
        self.thuis_team = thuis_team
        self.uit_team = uit_team
        self.thuis_doelpunten = None
        self.uit_doelpunten = None

    def uitslag(self, thuis_doelpunten, uit_doelpunten):
        self.thuis_doelpunten = thuis_doelpunten
        self.uit_doelpunten = uit_doelpunten

#----------------------------------------

club_ADO = Club('ADO', 'Den Haag')
club_PSV = Club('PSV', 'Eindhoven')
club_AJAX = Club('Ajax', 'Amsterdam')

team = Team('Eerste elftal')

speler1 = Speler('Johan Cruijf', 14, 'spits')
speler2 = Speler('Kees', 13, 'keeper')
speler3 = Speler('Jan', 15, 'verdediger')

team.speler_toevoegen(speler1, speler2, speler3)
club_ADO.team_toevoegen(team)


team = Team('Eerste elftal')

speler1 = Speler('Piet', 9, 'spits')
speler2 = Speler('van Haneigem', 7, 'keeper')
speler3 = Speler('Luke', 4, 'verdediger')

team.speler_toevoegen(speler1, speler2, speler3)

club_AJAX.team_toevoegen(team)

print('OK')