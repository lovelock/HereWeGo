#!/usr/bin/env python3
# encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication

from AddressBook import AddressBook

if __name__ == '__main__':
    app = QApplication(sys.argv)

    addressBook = AddressBook()
    addressBook.show()

    sys.exit(app.exec_())
