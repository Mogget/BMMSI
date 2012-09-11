# -*- coding: utf-8 -*-
"""

Obsługa okna użytkownika

"""

from datetime import datetime

from PyQt4 import QtGui
from PyQt4.QtCore import QDir
from PyQt4.QtGui import QWidget, QMessageBox

from bmmsi_ui import Ui_Form
from czest import GenratorPlikuTestowego, czestotliwosc
from silnik import SSN

class BmmsiWindow(QWidget):
    """
    Klasa obsługi interfejsu graficznego.
    Tworzy i zarządza oknem apliakcji.
    
    """
    
    
    def __init__(self, parent=None):
        """
        Konstruktor klasy okna.
        Tworzy okno widoczne na ekranie i połączenia przycisków w stylu Qt.
        
        """
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.ib_zbiorTreningowy.clicked.connect(self.chooseFolder)
        self.ui.ib_zbudujTrenujSiec.clicked.connect(self.generateTrainSet)
        self.ui.ib_testuj.clicked.connect(self.testCustomText)
        self.ui.o_zbiorTreningowy.setText(
            QDir.currentPath()+QDir.separator()+u"testFolder")
        
        # Na początku nie mamy zadnej sieci
        self.siec_neuronowa = None
        
        
    def chooseFolder(self):
        """ 
        Obsluga wyboru polozenia katalogu z danymi testowymi
        
        """
        dir = QtGui.QFileDialog.getExistingDirectory()
        self.ui.o_zbiorTreningowy.setText(dir)
        
        
    def generateTrainSet(self):
        """
        Gerneruje zestaw treningowy.
        Przeprowadza naukę sieci neuronowej.
        Parametry treningu sieci są pobierane z elementów GUI.

        Uwaga: Każdorazowo sieć tworzona jest na nowo.
        
        """
        
        if len (self.ui.o_zbiorTreningowy.text()) == 0:
            QMessageBox.warning(None, "BMMSI", u"Należy podać istniejącą scieżkę")
            return
        
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
                                  
        self.siec_neuronowa.logEntry.connect(self.addLineToLog)
        
        self.siec_neuronowa.train((QDir.currentPath()+QDir.separator()+"test.txt"),
                                  liczbaEpok=self.ui.i_liczbaEpok.value(),
                                  N=self.ui.i_wspolczynnikUczenia.value(),
                                  M=self.ui.i_wspolczynnikMomentum.value(),
                                  min_blad = self.ui.i_limiWartosciBledu.value() )
                                  
        self.ui.ib_testuj.setEnabled(True)
                                 

    def testCustomText(self):
        """
        Przeprowadza test dla wprowadzonego tekstu.
        
        """
        
        if len(self.ui.i_tekstWejsciowy.toPlainText()) == 0:
            QMessageBox.warning(None, "BMMSI", u"Należy podać tekst.")
            return

        wyn = [0,0,0,0]
        wyn = self.siec_neuronowa.test(czestotliwosc( self.ui.i_tekstWejsciowy.toPlainText()  ) )
        self.ui.o_en.setValue(wyn[0]*100  if wyn[0] > 0 else 0)
        self.ui.o_de.setValue(wyn[1]*100  if wyn[1] > 0 else 0)
        self.ui.o_pl.setValue(wyn[2]*100  if wyn[2] > 0 else 0)
        self.ui.o_fr.setValue(wyn[3]*100  if wyn[3] > 0 else 0)
        
    def addLineToLog(self, what):
        """
        Dodaje informacje do pola "log"
        
        """
        self.ui.o_log.appendPlainText('['+str(datetime.now())+'] ' + what)
        