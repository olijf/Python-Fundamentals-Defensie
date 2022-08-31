class card:

    def __init__(self):
        self.red: []
        self.yellow: []
        self.green: []
        self.blue: []
        self.forfeit: 0
        self.total_red: 0
        self.total_yellow: 0
        self.total_green: 0
        self.total_blue: 0
        self.total_forfeit: 0
        self.score: 0

    def mark(self, cell):
        """
        Mark of a cell on a Qwixx card
        :param card: The card to use
        :param cell: The cell to mark off. E.g. 'b2', 'r8'
        :return: None
        """
        print('Marking cell ' + cell)

        color = cell[0]

        if color == 'x':
            card['forfeit'] += 1
            return True

        number = int(cell[1:])

        if number < 2 or number > 12:
            print('Alleen getallen tussen 2 en 12 zijn toegestaan.')
            return False

        d = {'r': {'numbers': self.red, 'direction': 'up'},
             'y': {'numbers': self.yellow, 'direction': 'up'},
             'g': {'numbers': self.green, 'direction': 'down'},
             'b': {'numbers': self.blue, 'direction': 'down'}}

        numbers = d[color]['numbers']
        direction = d[color]['direction']

        valid = True
        if direction == 'up':
            if number > max([1] + numbers):
                numbers.append(number)
            else:
                print(f'Can only mark numbers higher than {max(numbers)}')
                return False

        elif direction == 'down':
            if number < min([13] + numbers):
                numbers.append(number)
            else:
                print(f'Can only mark numbers lower than {min(numbers)}')
                return False

        return True


    def score(self):
        points = {
            0: 0,
            1: 1,
            2: 3,
            3: 6,
            4: 10,
            5: 15,
            6: 21,
            7: 28,
            8: 36,
            9: 45,
            10: 55,
            11: 66,
            12: 78
        }

        self.total_red = points[len(self.red)]
        self.total_yellow = points[len(self.yellow)]
        self.total_green = points[len(self.green)]
        self.total_blue = points[len(self.blue)]
        self.total_forfeit = self.forfeit * 5

        self['score'] = self.total_red + \
                        self.total_yellow + \
                        self.total_green + \
                        self.total_blue - \
                        self.total_forfeit

