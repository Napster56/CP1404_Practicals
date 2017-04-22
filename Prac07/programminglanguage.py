"""
CP1404 Practical - Create a class for a programming language.
..
"""


class ProgrammingLanguage:
    """ProgrammingLanguage class - intermediate exercise."""

    def __init__(self, name='', typing='Static', reflection='', year=0):
        """Initialise a ProgrammingLanguage instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if language is dynamically typed or not."""
        if self.typing == 'Dynamic':
            return True
        else:
            return False

    def __getitem__(self, item):
        self.is_dynamic()

    def __str__(self):
        return "{},  {} Typing, Reflection= {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                             self.year)
