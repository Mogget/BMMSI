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
            
        self.siec_neuronowa = SSN( 2 + self.ui.i_iloscWarstwUkrytych.value(), 
                                  # wejściowa + wyjściowa + ukryte
                                  [ 25,
                                   self.ui.i_liczbaNeuronowWarstwaUkryta.value(),
                                    4,                                
                                  ]
                                  )
        self.siec_neuronowa.train((QDir.currentPath()+QDir.separator()+"test.txt"),
                                  liczbaEpok=self.ui.i_liczbaEpok.value(),
                                  N=self.ui.i_wspolczynnikUczenia.value(),
                                  M=self.ui.i_wspolczynnikMomentum.value())
        
#TODO: dzialaja tylko znaki ascii ;/
        tekstDe = 'Ein neuer Renner der Fernsehindustrie heist "Big Brother". Es gengt nicht, da viele Menschen ihre eigene, oft traurige, Realitt verdrngen, indem sie mit bewundernswerter Disziplin die Schicksale der Serienhelden verfolgen. Nein. Die Massen ergtzen sich neuerdings an dem tristen Alltag einiger in einem Container eingeschlossenen Leute. Sie beobachten die neuen Kultfiguren beim Rasieren oder Zhneputzen, hren langweiligen Gesprchen zu und warten auf einen Knller, eine Sensation.'
        tekstEn = 'If you take a look at the average day of the average family you would be surprised by the amount of time they spend watching TV. Films, quizes, news, soap operas, shows and sport - all in one in a little box in your home that is waiting for you to press the button. There is no doubt about it, TV attracts its viewers in every possible'
        tekstPl = 'ąęźćńBrytyjski aktor znany z roli Remisa Lupina z filmowej serii przygd Harryego Pottera. David Thewlis wcieli si w posta dilera informacji, znanego jako The Frog. Bohater zaczerpnie swj pseudonim po tym, jak zatruje wod w budynku Kremla przy pomocy egzotycznej aby z Amazonii. W kontynuacji filmu z 2010 roku, ujrzymy znw emerytowanych agentw CIA, w osobach Brucea Willisa, Helen Mirren i Johna Malkoicha, ktrzy uyj swojego dowiadczenia, aby ciga bandytw na terenie Europy. Swj udzia w "Red 2" potwierdzili take Catherine Zeta-Jones i Anthony Hopkins.'
        tekstFr = 'Bien sur, dit le renard. Tu nes encore pour moi quun petit garon tout semblable a cent mille petits garons. Et je nai pas besoin de toi. Et tu nas pas besoin de moi non plus. Je ne suis pour toi quun renard semblable a cent mille renards. Mais, si tu mapprioises, nous aurons besoin lun de lutre. Tu seras pour moi unique au monde. Je serai pour toi unique au monde'
        self.siec_neuronowa.test(czestotliwosc(tekstEn))
        self.siec_neuronowa.test(czestotliwosc(tekstDe))
        self.siec_neuronowa.test(czestotliwosc(tekstPl))
        self.siec_neuronowa.test(czestotliwosc(tekstFr))