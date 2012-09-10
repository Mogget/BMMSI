# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:13:31 2012

@author: bzyx
"""

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget
from czest import GenPlikuTestowego

from bmmsi_ui import Ui_Form

class BmmsiWindow(QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.ib_zbiorTreningowy.clicked.connect(self.chooseFolder)
        self.ui.ib_zbudujTrenujSiec.clicked.connect(self.generateTrainSet)
        
    def chooseFolder(self):
        dir = QtGui.QFileDialog.getExistingDirectory()
        self.ui.o_zbiorTreningowy.setText(dir)
        
    def generateTrainSet(self):
        gen = GenPlikuTestowego()
        gen.generuj(self.ui.o_zbiorTreningowy.text())