"""
CP1404 Practical 8 - Inheritance
Client code to use the UnreliableCar class.
"""

from taxi import UnreliableCar


def main():
    """ Code to use UnreliableCar class """

    my_car = UnreliableCar('Valiant', 80)
    my_car.drive(65)
    print(my_car)
    my_car.drive(10)
    my_car.add_fuel(70)
    my_car.drive(45)
    print(my_car)


main()

