# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:13:31 2012

@author: bzyx
"""

from PyQt4 import QtGui
from PyQt4.QtCore import QDir
from PyQt4.QtGui import QWidget
from czest import GenratorPlikuTestowego, czestotliwosc

from bmmsi_ui import Ui_Form
from silnik import SSN

class BmmsiWindow(QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.ib_zbiorTreningowy.clicked.connect(self.chooseFolder)
        self.ui.ib_zbudujTrenujSiec.clicked.connect(self.generateTrainSet)
        self.ui.ib_testuj.clicked.connect(self.testCustomText)
        self.ui.o_zbiorTreningowy.setText(QDir.currentPath()+QDir.separator()+u"testFolder")
        
        
        self.siec_neuronowa = None
        
    def chooseFolder(self):
        dir = QtGui.QFileDialog.getExistingDirectory()
        self.ui.o_zbiorTreningowy.setText(dir)
        
    def generateTrainSet(self):
        gen = GenratorPlikuTestowego()
        gen.generuj(self.ui.o_zbiorTreningowy.text())
        
        if self.siec_neuronowa is not None:
            del self.siec_neuronowa
            self.siec_neuronowa = None
            
        ssn_params = [25,] #wartstwa wejściowa
        # warstwy ukryte
        for x in range(self.ui.i_iloscWarstwUkrytych.value()):
            ssn_params.append(self.ui.i_liczbaNeuronowWarstwaUkryta.value())
        # warstwa wyjściowa
        ssn_params.append(4)
        self.siec_neuronowa = SSN( 2 + self.ui.i_iloscWarstwUkrytych.value(), 
                                  ssn_params,
                                  )
        self.siec_neuronowa.train((QDir.currentPath()+QDir.separator()+"test.txt"),
                                  liczbaEpok=self.ui.i_liczbaEpok.value(),
                                  N=self.ui.i_wspolczynnikUczenia.value(),
                                  M=self.ui.i_wspolczynnikMomentum.value())

    def testCustomText(self):
        print str(self.ui.i_tekstWejsciowy.toPlainText())
        wyn = self.siec_neuronowa.test(czestotliwosc( self.ui.i_tekstWejsciowy.toPlainText()  ) )
        self.ui.o_en.setValue(wyn[0]*100)
        self.ui.o_de.setValue(wyn[1]*100)
        self.ui.o_pl.setValue(wyn[2]*100)
        self.ui.o_fr.setValue(wyn[3]*100)
        