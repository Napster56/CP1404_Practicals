"""
CP1404 Practical 8 - Inheritance
Client code to use the Taxi class.
"""

import taxi


def main():
    """ Code to use Taxi class """

    my_taxi = taxi.Taxi('Prius', 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    my_taxi.add_fuel(65)
    my_taxi.start_fare()
    my_taxi.drive(45)
    print(my_taxi)



main()

