"""
CP1404 Prac07 - Create a class for guitars.
"""


class Guitar:
    """Guitar class - intermediate exercise."""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a Guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2017 - int(self.year)
        return age

    def is_vintage(self, age):
        if age >= 50:
            return True
        else:
            return False

    def __str__(self):
        return "{} {} : ${:.2f}". format(self.name, self.year, self.cost)



