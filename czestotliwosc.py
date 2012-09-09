#!/usr/bin/env python
import os
import random


class GenPlikuTestowego(object):
    """generator pliku testowego"""
    testFolder = '.'+os.sep+'testFolder'+os.sep

    def __init__(self):
        super(GenPlikuTestowego, self).__init__()
        self.fLiter = {}      # czestotliwosc liter
        self.suma = .0
        self.skrotyPanstw = ['an', 'de', 'pl', 'fr']
        self.litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
                'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'q', 'x', 'y', 'z']
                
        print self.testFolder
        os.remove('test.txt')

    def czestotliwosc(self, nazwaPliku):
        """funkcja liczaca czestotliwosc wystepowania liter w pliku"""
        plik = open(self.testFolder + nazwaPliku)
        try:
            tekst = plik.read()
        finally:
            plik.close()
        tekst.lower()
        for litera in self.litery:
            self.fLiter[litera] = (tekst.count(litera))
        for ile in self.fLiter.values():
            self.suma += float(ile)
        self.wyjscie()

    def wyjscie(self):
        """funkcja zwracajaca plik wynikowy"""
        plik = open('test.txt', 'a')
        tekst = ''
        for wartosc in self.litery:
            tekst += str(float(self.fLiter[wartosc]) / self.suma) + ' '
        plik.write(tekst + '\n')
        plik.close()
        self.fLiter.clear()
        self.suma = 0.0

    def podsumowanieTestu(self, tekst):
        """docstring for posumowanieTestu"""
        plik = open('test.txt', 'a')
        plik.write(tekst + '\n\n')
        plik.close()
    
    def generuj(self, dir = testFolder):
        """generuje plik testowy"""
        pliki = os.listdir(dir)
        print pliki
        random.shuffle(pliki)
        self.podsumowanieTestu(str(len([lista for lista in pliki if lista[:2] in self.skrotyPanstw])) +\
                ' 26 ' + str(len(self.skrotyPanstw)))
        for plik in pliki:
            tekst = ''
            if (plik[:2]) in self.skrotyPanstw:
                self.czestotliwosc(plik)
                for ilePanstw in range(len(self.skrotyPanstw)):
                    if ilePanstw == self.skrotyPanstw.index(plik[:2]):
                        tekst += '1 '
                    else:
                        tekst += '0 '
                self.podsumowanieTestu(tekst)
    
if __name__ == "__main__":
    gen = GenPlikuTestowego()
    gen.generuj()
