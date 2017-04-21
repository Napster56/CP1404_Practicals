"""
CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of list
Modified from dynamic_widgets, 20/04/2017
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

__author__ = 'Tyrone Napoli'


class DynamicWidgetsApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        # basic data example - list of composers
        self.composer_list = ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven",
                              "Frederic Chopin", "Igor Stravinsky"]

    def build(self):
        """

        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Display Strings"
        self.root = Builder.load_file('display_strings.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.composer_list:
            # create a button for each phonebook entry
            temp_button = Button(text=name)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)


DynamicWidgetsApp().run()

