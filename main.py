#!/usr/bin/python

# Author: n-anselm
# Date created: 221108
# Date modified: 221108
# Description: Qt GUI application which takes any positive integer, replaces the
# number by the sum of the squares of its digits, and repeats the process until
# the number is 1, or loops in a cycle (max loops set to 100) which does not
# produce 1. A number is a "happy number" if the process produces 1.

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from WindowUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCheck.clicked.connect(self.check)  # Call check() method when clicked

    # Find out if a number is a "happy number" or not
    def check(self):
        num_input = self.ui.leNumber.text()  # Input text
        lab_output = self.ui.labOutput  # Output message label

        # Input checking (program will not throw errors without this)
        if num_input == "":
            lab_output.setText("Please enter a number")
            return False

        number = 0

        for n in num_input:
            number += int(n) ** 2

        counter = 0
        while True:
            tmpnum = 0

            for i in str(number):
                tmpnum += int(i) ** 2

            number = tmpnum
            # print(number)  # DEBUG

            if number == 1:
                lab_output.setText(num_input + " is a happy number!")
                return False
            elif counter > 100:  # Iterations set to max 100
                lab_output.setText(num_input + " is not a happy number")
                return False
            else:
                counter += 1


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
