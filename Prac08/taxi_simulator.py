"""
CP1404 Practical 8 - Inheritance
Client code to use the Taxi and SilverServiceTaxi class.
"""

from silver_taxi import SilverServiceTaxi
from taxi import Taxi

MENU_CHOICES = ["c", "d", "q"]


def display_menu():
    print("q)uit, c)hoose taxi, d)rive")


def get_choice():
    choice = input().lower()
    while choice not in MENU_CHOICES:
        print("Invalid menu choice")
        display_menu()
        choice = input().lower()
    return choice


def display_taxi_list(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(i, taxi)


def get_distance(my_taxi):
    distance = int(input("Drive how far?"))
    my_taxi.drive(distance)


def choose_taxi(my_bill, taxis):
    my_taxi = int(input("Choose taxi: "))
    if my_taxi == 0:
        my_taxi = taxis[0]
        print("Bill to date: ${:.2f}".format(my_bill))
        get_distance(my_taxi)
        calculate_bill(my_taxi)
    elif my_taxi == 1:
        my_taxi = taxis[1]
        print("Bill to date: ${:.2f}".format(my_bill))
        get_distance(my_taxi)
        calculate_bill(my_taxi)
    else:
        my_taxi = taxis[2]
        print("Bill to date: ${:.2f}".format(my_bill))
        get_distance(my_taxi)
        calculate_bill(my_taxi)



def calculate_bill(my_taxi):
    my_bill = my_taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(my_taxi.name, my_bill))
    print("Bill to date: ${}".format(my_bill))
    display_menu()
    get_choice()


def process_menu_selection(choice, taxis):
    while choice != "q":
        if choice == "c":
            my_bill = 0
            display_taxi_list(taxis)
            choose_taxi(my_bill, taxis)
        elif choice == "d":
            trip_distance = get_distance()
            return trip_distance

    return


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    display_menu()
    choice = get_choice()
    my_taxi = process_menu_selection(choice, taxis)
    calculate_bill(my_taxi)


main()
