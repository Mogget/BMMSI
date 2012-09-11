# -*- coding: utf-8 -*-

import os
import random

from const import obslugiwane_litery, skroty_panstw, PLIK_TRENINGOWY


def czestotliwosc(tekst):
    suma = 0
    wynik = []
    czest_litery = []

    for wartosc in obslugiwane_litery:
        suma += float(tekst.count(wartosc))
        czest_litery.append(float(tekst.count(wartosc)))

    for wartosc in czest_litery:
        wynik.append(wartosc / suma)

    return wynik


class GenratorPlikuTestowego(object):
    """generator pliku testowego"""
    testFolder = '.' + os.sep + 'testFolder' + os.sep

    def __init__(self):
        super(GenratorPlikuTestowego, self).__init__()
        self.czest_liter = [] # czestotliwosc liter
        self.suma = float(0)

        # usuwanie starego pliku
        if os.path.exists(PLIK_TRENINGOWY):
            os.remove(PLIK_TRENINGOWY)

    def obliczCzestotliwoscPliku(self, nazwa_pliku):
        with open(self.testFolder + nazwa_pliku) as f:
            zawartosc = f.read().lower()
            
            self.czest_liter = czestotliwosc(zawartosc)
            self.wyjscie()

    def wyjscie(self):
        """funkcja zwracajaca plik wynikowy"""
        tekst = str()
        
        with open(PLIK_TRENINGOWY, 'a') as plik:
            for elem in self.czest_liter:
                tekst += str(elem) + ' '
        
            plik.write(tekst + '\n')

        self.czest_liter = []

    def podsumowanieTestu(self, tekst):
        """docstring for posumowanieTestu"""
        with open(PLIK_TRENINGOWY, 'a') as plik:
            plik.write(tekst + '\n\n')
  
    def generuj(self, dir=testFolder):
        """generuje plik testowy"""
        pliki_testowe = os.listdir(dir)
        #FIXME: co robi te shuffle tu?
        random.shuffle(pliki_testowe)
        #FIXME: tej linii nie rozumiem
        self.podsumowanieTestu(str(len([lista for lista in pliki_testowe if lista[:2] in skroty_panstw])) +\
                ' ' + str(len(obslugiwane_litery)) + ' ' + str(len(skroty_panstw)))
        
        for plik in pliki_testowe:
            tekst = ''
            if (plik[:2]) in skroty_panstw:
                self.obliczCzestotliwoscPliku(plik)
                for ilePanstw in range(len(skroty_panstw)):
                    if ilePanstw == skroty_panstw.index(plik[:2]):
                        tekst += '1 '
                    else:
                        tekst += '0 '
                self.podsumowanieTestu(tekst)
    
if __name__ == "__main__":
    gen = GenratorPlikuTestowego()
    gen.generuj()