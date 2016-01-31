#!/usr/bin/env python3
# encoding: utf-8

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        hello = 'hello'
        world = 'world'

        label = QLabel(hello + world)
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

