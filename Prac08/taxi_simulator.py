"""
CP1404 Practical 8 - Inheritance
Client code to use the Taxi and SilverServiceTaxi class.
Program asks the user to select from a menu; user can choose to quit, choose a taxi and drive
the taxi. Program displays a list of available taxis, the trip cost, the bill to date and
the total trip cost on quit.
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
        print(i, "-", taxi)


def get_distance(my_taxi):
    distance = int(input("Drive how far?"))
    my_taxi.drive(distance)


def choose_taxi(my_taxi, taxis):
    if my_taxi == 0:
        my_taxi = taxis[0]
        display_menu()
    elif my_taxi == 1:
        my_taxi = taxis[1]
        display_menu()
    else:
        my_taxi = taxis[2]
        display_menu()
    return my_taxi


def calculate_total_bill(my_taxi, total_bill):
    total_bill += my_taxi.get_fare()
    return total_bill


def calculate_bill(my_taxi):
    my_taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(my_taxi.name, my_taxi.get_fare()))


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    display_menu()
    choice = get_choice()
    while choice != "q":
        if choice == "c":
            display_taxi_list(taxis)
            my_taxi = int(input("Choose taxi:"))
            print("Bill to date: ${:.2f}".format(total_bill))
            my_taxi = choose_taxi(my_taxi, taxis)
            choice = get_choice()
        elif choice == "d":
            get_distance(my_taxi)
            calculate_bill(my_taxi)
            total_bill = calculate_total_bill(my_taxi, total_bill)
            print("Bill to date: ${:.2f}".format(total_bill))
            display_menu()
            choice = get_choice()

    print("Total trip cost: ${}".format(total_bill))
    display_taxi_list(taxis)

main()
