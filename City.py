#!/usr/bin/env python2.7

import json
import re
import sys
import os
import operator

from PySide.QtGui import *
from CityInfo import *


class City(QMainWindow, Ui_Dialog):
    # initializations for GUI and various text boxes and buttons
    def __init__(self, parent=None):

        super(City, self).__init__(parent)
        self.setupUi(self)
        self.city_dict = {}
        self.City_Drop.currentIndexChanged.connect(self.load_from_dict)
        self.pushButton.clicked.connect(self.load_from_file)
        self.pushButton.setDisabled(True)
        self.text_Filename.textChanged.connect(self.set_push_button)

    ''' Function to load the information of any city in the drop down list
        from the dictionary that contains the relevant information '''
    def load_from_dict(self):
        city_name = str(self.City_Drop.currentText())
        self.text_county.setText(self.city_dict[city_name]['full_county_name'])
        self.text_lat.setText(self.city_dict[city_name]['primary_latitude'])
        self.text_long.setText(self.city_dict[city_name]['primary_longitude'])

    # Function to parse the JSON file given by the user and load data into the dictionary of the City class
    def load_from_file(self):
        file_pattern = r'.+\.json$'  # simple regex to check whether the input file is of type .json
        filename = self.text_Filename.text()

        # Error checking to make sure filename given by user is of type .json
        if not re.match(file_pattern, filename):
            self.label_error.setText('Error: Input file not of type .json')
        # Error checking to make sure that the file inputted by the user exists
        elif not os.path.isfile(filename):
            self.label_error.setText('Error: Input file not found')
        # File is found and is of type .json, parse JSON objects and load them into a dictionary
        else:
            with open(filename, 'r') as file_pointer:
                # parse JSON objects and store in a list and sort list by name of city
                json_raw = file_pointer.readline()
                city_information_list = json.loads(json_raw)
                city_information_list.sort(key=operator.itemgetter('name'))

            ''' Populate drop down with city names and
                also the city dictionary with the key: city name and value: dictionary of city information
                Also do not add dictionaries with county_names and full_count_names = None as they are most
                likely counties themselves.'''
            for dictionary in city_information_list:
                if dictionary['county_name'] is not None and dictionary['full_county_name'] is not None:
                    self.city_dict[dictionary['name']] = dictionary
                    self.City_Drop.addItem(dictionary['name'])

    # Function to enable or disable the load json button
    def set_push_button(self):
        self.label_error.setText('')

        # If filename field is empty, disable button, otherwise enable it
        if self.text_Filename.text() == '':
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = City()

    currentForm.show()
    currentApp.exec_()
