"""
CP1404 Practical 8 - Inheritance
Client code to use the Taxi and SilverServiceTaxi class.
"""

from silver_taxi import SilverServiceTaxi
from taxi import Taxi

MENU_CHOICES = ["c", "d", "q"]


def display_menu():
    print("Let's drive!\nq)uit, c)hoose taxi, d)rive")


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


def get_distance():
    distance = int(input("Drive how far?"))
    return distance


def choose_taxi(my_bill):
    my_taxi = int(input("Choose taxi: "))
    if my_taxi == 0:
        print("Bill to date: ${:.2f}".format(my_bill))
    elif my_taxi == 1:
        print("Bill to date: ${:.2f}".format(my_bill))
    else:
        print("Bill to date: ${:.2f}".format(my_bill))
    return my_taxi


def calculate_bill(my_taxi):
    my_bill = 0
    return my_bill


def process_menu_selection(choice, taxis):
    while choice != "q":
        if choice == "c":
            display_taxi_list(taxis)
            choose_taxi(my_bill=0)
        elif choice == "d":
            trip_distance = get_distance()
            return trip_distance

    return


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    display_menu()
    choice = get_choice()
    process_menu_selection(choice, taxis)


main()
