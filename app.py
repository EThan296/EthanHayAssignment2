__author__ = 'jc319762 - Ethan Hay - Ethan.hay@my.jcu.edu.au'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from currency import convert, get_all_details, get_details
import time
import trip



class ForeignExchangeCalculator(App):
    # ForeignExchangeCalculator is a Kivy App for converting currency
    country_list = ListProperty()
    current_country = StringProperty()
    locations = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rate = 0

    def build(self):
        # Load Kivy app
        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.root.ids.txt_foreign_amount.disabled = True
        self.root.ids.txt_home_amount.disabled = True
        self.root.ids.lbl_date.text = "Today is: " + time.strftime("%d/%m/%Y")
        self.load_configfile()
        self.country_list = sorted(self.locations)
        return self.root

    def load_currency(self, direction):
        try:
            if direction == "foreign":
                amount = self.root.ids.txt_foreign_amount.text
                result = int(amount) / self.rate
                result = round(result, 3)
                result = str(result)
                self.root.ids.txt_home_amount.text = result
                self.root.ids.lbl_error.text = "{} ({}) to {} ({})".format(self.target_currency[1],self.target_currency[2],self.home_currency[1],self.home_currency[2])
            elif direction == "home":
                amount = self.root.ids.txt_home_amount.text
                result = int(amount) * self.rate
                result = round(result, 3)
                result = str(result)
                self.root.ids.txt_foreign_amount.text = result
                self.root.ids.lbl_error.text = "{} ({}) to {} ({})".format(self.home_currency[1],self.home_currency[2],self.target_currency[1],self.target_currency[2])
        except:
            self.root.ids.lbl_error.text = "Error: Number error"
            self.root.ids.txt_foreign_amount.disabled = True
            self.root.ids.txt_home_amount.disabled = True

    def load_data(self):
        # load date and store in label, set last updated time
        self.root.ids.lbl_date.text = "Today is: " + time.strftime("%Y/%m/%d")
        self.root.ids.lbl_status.text = "Last updated: " + time.strftime("%H:%M:%S") + "\n" + time.strftime("%Y/%m/%d")
        # start conversion, store rate, Enable Textinput, if something goes wrong they will be disabled
        self.root.ids.txt_foreign_amount.disabled = False
        self.root.ids.txt_home_amount.disabled = False
        self.home_currency = get_details(self.root.ids.lbl_home_country.text)
        self.target_currency = get_details(self.root.ids.country_spinner.text)
        if self.root.ids.country_spinner.text != "":
            try:
                self.rate = convert(1, self.home_currency[1], self.target_currency[1])
            except:
                self.root.ids.lbl_error.text = "Error: Null Rate"
                self.root.ids.txt_foreign_amount.disabled = True
                self.root.ids.txt_home_amount.disabled = True
        else:
            self.root.ids.country_spinner.text = self.current_country
            # self.root.ids.lbl_error.text = "Error: Select a country"
            # self.root.ids.txt_foreign_amount.disabled = True
            # self.root.ids.txt_home_amount.disabled = True

    def change_country(self, country):
        # handle change of output result to label widget
        self.root.ids.lbl_error.text = "Changed to: " + country
        self.load_data()

    def clear_error_lbl(self):
        self.root.ids.lbl_error.text = ""

    def load_configfile(self):
        try:
            self.details = trip.Details()
            with open("config.txt", encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines[1:]:
                    country, start_date, end_date = line.strip().split(',')
                    self.locations.append(country)
                    trips = (country, start_date, end_date)
                    self.details.add(*trips)
            current_date = time.strftime("%Y/%m/%d")
            try:
                self.current_country = self.details.current_country(current_date)
            except:
                self.root.ids.lbl_error.text = "Config file - Invalid Details"
            current_country_string = "Your current country is:\n" + self.current_country
            self.root.ids.lbl_current_location.text = current_country_string
            # self.root.ids.country_spinner.values = self.locations()
            f.close()
            home_country = lines[:1]
            home_country = str(home_country)[2:-4]
            self.root.ids.lbl_home_country.text = home_country

            #success message
            self.root.ids.lbl_error.text = "Config file - Success!"
        except:
            self.root.ids.lbl_error.text = "Config file - Not loaded!"


ForeignExchangeCalculator().run()
