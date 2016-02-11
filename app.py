#!/usr/bin/env python3
# encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication

from Form import Form

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec_())
