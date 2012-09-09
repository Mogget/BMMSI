# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:13:31 2012

@author: bzyx
"""

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget

from bmmsi_ui import Ui_Form

class BmmsiWindow(QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)