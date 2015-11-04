__author__ = 'jc319762'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ForeignExchangeCalculator(App):
    """ ForeignExchangeCalculator is a Kivy App for converting currency """
    # def __init__(self):
        # pass

    def build(self):
        """     Load Kivy app       """
        Window.size = (350, 700)
        # Window.clearcolor = (255, 255, 255, 0)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def load_currency(self):
        home_currency = self.root.ids.lbl_home_country.text

ForeignExchangeCalculator().run()








# things that need to be done
    # TextInput widgets are initially disabled
    # Button  --->  currency.convert  ---> stores 2 conversion rates
    # Spinner --->  currency.convert  ---> stores 2 conversion rates
    # Update lbl_status

# Things to note:
#     If the Button is pressed and no Spinner selection has been made yet,
#       then the current date determines the current trip location
#       which sets the selected country name for the Spinner
#     If the Spinner selection is a country name with the same currency as
#       the the previously selected country, then there is no need to update the conversion rates
#     If a conversion rate update fails then the TextInput widgets should be disabled
#       (enable them again when the next conversion rate update succeeds)

#   When the user enters a monetary value into a TextInput and hits ENTER
#   the appropriate conversion rate is used to set the text of the other TextInput with the converted amount

# Things to note:
#     The updated TextInput shows the converted amount as a float with 3 significant digits
#     When the user starts typing into a TextInput widget the status Label is cleared
#     After the conversion the status Label shows the direction of the conversion:


# other requirements

# documentation/evaluation of code

# submission
#
