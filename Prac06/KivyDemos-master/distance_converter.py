"""
CP1404 Practical06
Kivy GUI program to convert distance in miles to km
Tyrone Napoli, IT@JCU
Started 19/04/2017
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Tyrone napoli'


MILES_TO_KM = 1.60934


class DistanceConverterApp(App):
    """ DistanceConverterApp is a Kivy App for converting distance in miles to km """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

    def handle_convert(self):
        """ handle conversion (could be button press or other call), output result to label widget"""
        value = self.validate_input()
        result = int(value) * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """ handle increment (on button press)"""
        value = self.validate_input() + increment
        self.root.ids.input_number.text = str(value)

    def validate_input(self):
        """ error handling for input value; if ValueError occurs return 0 """
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


DistanceConverterApp().run()
