"""
CP1404 Prac07 - Create a class for guitars.
"""

import datetime

class Guitar:
    """Guitar class - intermediate exercise."""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a Guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __str__(self):
        return "{} {} : ${:.2f}". format(self.name, self.year, self.cost)



