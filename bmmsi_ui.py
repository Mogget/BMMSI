# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmmsi.ui'
#
# Created: Sun Sep  9 18:55:48 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(740, 700)
        Form.setMinimumSize(QtCore.QSize(740, 700))
        Form.setMaximumSize(QtCore.QSize(740, 700))
        self.gridLayout_3 = QtGui.QGridLayout(Form)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.i_iloscWarstwUkrytych = QtGui.QSpinBox(self.groupBox)
        self.i_iloscWarstwUkrytych.setObjectName(_fromUtf8("i_iloscWarstwUkrytych"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.i_iloscWarstwUkrytych)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.i_liczbaNeuronowWarstwaUkryta = QtGui.QSpinBox(self.groupBox)
        self.i_liczbaNeuronowWarstwaUkryta.setObjectName(_fromUtf8("i_liczbaNeuronowWarstwaUkryta"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.i_liczbaNeuronowWarstwaUkryta)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.i_liczbaEpok = QtGui.QSpinBox(self.groupBox)
        self.i_liczbaEpok.setObjectName(_fromUtf8("i_liczbaEpok"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.i_liczbaEpok)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.i_sredniBladEpoki = QtGui.QDoubleSpinBox(self.groupBox)
        self.i_sredniBladEpoki.setObjectName(_fromUtf8("i_sredniBladEpoki"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.i_sredniBladEpoki)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.i_wspolczynnikUczenia = QtGui.QDoubleSpinBox(self.groupBox)
        self.i_wspolczynnikUczenia.setObjectName(_fromUtf8("i_wspolczynnikUczenia"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.i_wspolczynnikUczenia)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.i_uczenieNeuronu = QtGui.QSpinBox(self.groupBox)
        self.i_uczenieNeuronu.setObjectName(_fromUtf8("i_uczenieNeuronu"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.i_uczenieNeuronu)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_2.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        self.ic_sigmod = QtGui.QRadioButton(self.groupBox)
        self.ic_sigmod.setChecked(True)
        self.ic_sigmod.setObjectName(_fromUtf8("ic_sigmod"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.ic_sigmod)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_2.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.ic_log = QtGui.QRadioButton(self.groupBox)
        self.ic_log.setObjectName(_fromUtf8("ic_log"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.ic_log)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_2.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.ic_liniowa = QtGui.QRadioButton(self.groupBox)
        self.ic_liniowa.setObjectName(_fromUtf8("ic_liniowa"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.ic_liniowa)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.o_zbiorTreningowy = QtGui.QLineEdit(self.groupBox_2)
        self.o_zbiorTreningowy.setObjectName(_fromUtf8("o_zbiorTreningowy"))
        self.gridLayout.addWidget(self.o_zbiorTreningowy, 1, 0, 1, 1)
        self.ib_zbiorTreningowy = QtGui.QPushButton(self.groupBox_2)
        self.ib_zbiorTreningowy.setObjectName(_fromUtf8("ib_zbiorTreningowy"))
        self.gridLayout.addWidget(self.ib_zbiorTreningowy, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.ib_zbudujTrenujSiec = QtGui.QPushButton(self.groupBox_2)
        self.ib_zbudujTrenujSiec.setObjectName(_fromUtf8("ib_zbudujTrenujSiec"))
        self.verticalLayout_2.addWidget(self.ib_zbudujTrenujSiec)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.i_tekstWejsciowy = QtGui.QPlainTextEdit(self.groupBox_3)
        self.i_tekstWejsciowy.setObjectName(_fromUtf8("i_tekstWejsciowy"))
        self.gridLayout_2.addWidget(self.i_tekstWejsciowy, 2, 0, 1, 2)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.ib_testuj = QtGui.QPushButton(self.groupBox_3)
        self.ib_testuj.setObjectName(_fromUtf8("ib_testuj"))
        self.gridLayout_2.addWidget(self.ib_testuj, 3, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.o_wynik = QtGui.QLineEdit(self.groupBox_3)
        self.o_wynik.setObjectName(_fromUtf8("o_wynik"))
        self.gridLayout_2.addWidget(self.o_wynik, 6, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.o_log = QtGui.QPlainTextEdit(Form)
        self.o_log.setObjectName(_fromUtf8("o_log"))
        self.verticalLayout_3.addWidget(self.o_log)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "BMMSI - Wykrywanie języka", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "1) Konfiguracja", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Ilość warstw ukrytych", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Liczba neuronów w warstwie ukrytej", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Limit epok", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Średni błąd limitu epoki", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Współczynnik uczenia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Liczba uczenia nuronu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Funkcja", None, QtGui.QApplication.UnicodeUTF8))
        self.ic_sigmod.setText(QtGui.QApplication.translate("Form", "Sigmod", None, QtGui.QApplication.UnicodeUTF8))
        self.ic_log.setText(QtGui.QApplication.translate("Form", "Logarytmiczna", None, QtGui.QApplication.UnicodeUTF8))
        self.ic_liniowa.setText(QtGui.QApplication.translate("Form", "Liniowa", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "2) Trenning", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Zbiór treningowy", None, QtGui.QApplication.UnicodeUTF8))
        self.ib_zbiorTreningowy.setText(QtGui.QApplication.translate("Form", "Wybierz", None, QtGui.QApplication.UnicodeUTF8))
        self.ib_zbudujTrenujSiec.setText(QtGui.QApplication.translate("Form", "Zbuduj i trenuj sieć", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "3) Działanie", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Wynik", None, QtGui.QApplication.UnicodeUTF8))
        self.ib_testuj.setText(QtGui.QApplication.translate("Form", "Testuj", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Tekst wejściowy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Log", None, QtGui.QApplication.UnicodeUTF8))
