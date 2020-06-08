# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QLineEdit")
        self.resize(300, 50)
        lineEdit = QtGui.QLineEdit("Initial value")
        lineEdit.setAlignment(QtCore.Qt.AlignRight)
        box = QtGui.QVBoxLayout()
        box.addWidget(lineEdit)
        self.setLayout(box)
        self.show()