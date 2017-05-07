"""
CP1404 Practical 8 - Inheritance
This program extends the Car class with inheritance by creating a Taxi class
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """ sub-class of Taxi that includes an attribute for fanciness """
    flag_fall = 4.50     # class variable

    def __init__(self, name, fuel, fanciness=0.0):
        """ initialise a SilverServiceTaxi instance, based on class Taxi """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness    # update price_per_km with fanciness value

    def get_fare(self):
        """ get the price for the SilverServiceTaxi trip """
        return self.price_per_km * self.current_fare_distance + SilverServiceTaxi.flag_fall

    def __str__(self):
        """ return a string representation like a taxi but with fanciness included """
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flag_fall)
