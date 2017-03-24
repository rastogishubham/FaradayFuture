import json
import re
import sys
import os
import operator

from PySide.QtGui import *
from CityInfo import *


class City(QMainWindow, Ui_Dialog):

    def __init__(self, parent=None):

        super(City, self).__init__(parent)
        self.setupUi(self)
        self.city_dict = {}
        self.City_Drop.currentIndexChanged.connect(self.load_from_dict)
        self.pushButton.clicked.connect(self.load_from_file)
        self.pushButton.setDisabled(True)
        self.text_Filename.textChanged.connect(self.set_push_button)

    def load_from_dict(self):
        city_name = str(self.City_Drop.currentText())
        self.text_county.setText(self.city_dict[city_name]['full_county_name'])
        self.text_lat.setText(self.city_dict[city_name]['primary_latitude'])
        self.text_long.setText(self.city_dict[city_name]['primary_longitude'])
        return

    def load_from_file(self):

        file_pattern = r'.+\.json$'
        filename = self.text_Filename.text()
        if not os.path.isfile(filename):
            self.label_error.setText('Error: Input file not found')
        elif not re.match(file_pattern, filename):
            self.label_error.setText('Error: Input file not of type .json')
        else:
            with open(filename, 'r') as file_pointer:
                json_raw = file_pointer.readline()
                city_information_list = json.loads(json_raw)
                city_information_list.sort(key=operator.itemgetter('name'))
            for dictionary in city_information_list:
                self.city_dict[dictionary['name']] = dictionary
                self.City_Drop.addItem(dictionary['name'])

    def set_push_button(self):
        self.label_error.setText('')
        if self.text_Filename.text() == '':
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = City()

    currentForm.show()
    currentApp.exec_()
