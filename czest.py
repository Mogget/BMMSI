#!/usr/bin/env python
import os
import random

from const import obslugiwane_litery, skroty_panstw

def czestotliwosc(tekst):
    suma = 0
    wynik = []
    fLitera = []

    for wartosc in obslugiwane_litery:
        suma += float(tekst.count(wartosc))
        fLitera.append(float(tekst.count(wartosc)))

    for wartosc in fLitera:
        wynik.append(wartosc / suma)

    return wynik

class GenPlikuTestowego(object):
    """generator pliku testowego"""
    testFolder = '.'+os.sep+'testFolder'+os.sep

    def __init__(self):
        super(GenPlikuTestowego, self).__init__()
        self.fLiter = {}      # czestotliwosc liter
        self.suma = .0

        print self.testFolder
        os.remove('test.txt')

    def czestotliwoscPliku(self, nazwaPliku):
        """funkcja liczaca czestotliwosc wystepowania liter w pliku"""
        #FIXME: tu użycie funckcji czestoliwosc
        plik = open(self.testFolder + nazwaPliku)
        try:
            tekst = plik.read()
        finally:
            plik.close()
        tekst.lower()
        for litera in obslugiwane_litery:
            self.fLiter[litera] = (tekst.count(litera))
        for ile in self.fLiter.values():
            self.suma += float(ile)
        self.wyjscie()

    def wyjscie(self):
        """funkcja zwracajaca plik wynikowy"""
        plik = open('test.txt', 'a')
        tekst = ''
        for wartosc in obslugiwane_litery:
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
        random.shuffle(pliki)
        self.podsumowanieTestu(str(len([lista for lista in pliki if lista[:2] in skroty_panstw])) +\
                ' 25 ' + str(len(self.skrotyPanstw)))
        for plik in pliki:
            tekst = ''
            if (plik[:2]) in self.skrotyPanstw:
                self.czestotliwoscPliku(plik)
                for ilePanstw in range(len(self.skrotyPanstw)):
                    if ilePanstw == self.skrotyPanstw.index(plik[:2]):
                        tekst += '1 '
                    else:
                        tekst += '0 '
                self.podsumowanieTestu(tekst)
    
if __name__ == "__main__":
    gen = GenPlikuTestowego()
    gen.generuj()
