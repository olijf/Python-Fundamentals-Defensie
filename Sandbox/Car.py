class Car:

    def __init__(self, make, type, color):
        self._make = make
        self._type = type
        self._color = color
        self._mileage = 0

    def info(self):
        print( f'This great {self._color} {self._make} {self._type} as driven {self._mileage}km.' )

    def drive(self, km):
        self._mileage += km

# -------------------------------------------------------

my_car = Car('Renault', 'Megane', 'metalic brown')

my_car.drive(200)

print(my_car)
