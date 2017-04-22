"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac07.car import Car


def main():
    """Demo test code to show how to use car class."""

    bus = Car('bus', 180)
    bus.drive(30)
    limo = Car('limo', 100)
    limo.add_fuel(20)
    limo.drive(115)
    # print("fuel =", bus.fuel, limo.fuel)
    # print("odo =", bus.odometer)
    print(bus)
    # print("{self.name} {self.fuel}, {self.odometer}".format(self=limo))
    print(limo)


main()
