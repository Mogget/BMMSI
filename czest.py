# -*- coding: utf-8 -*-
"""
Obsługa genrowania częstoliwości.
Generowanie pliku testowego

"""

import os

from const import obslugiwane_litery, skroty_panstw, PLIK_TRENINGOWY


def czestotliwosc(tekst):
    """
    Oblicza częstoliwość zadanego tekstu wejściowego
    
    Zwraca listę częstoliwości występowania poszczególnych liter alfabetu.
    
    """
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
    """
    Klasa generująca plik treningowy na podstawie zawartości
    katalogu z plikami źródłowymi w odpowienich językach.
    
    """
    testFolder = '.' + os.sep + 'testFolder' + os.sep

    def __init__(self):
        """
        Konstruktor klasy
        
        Jeśli istnieje plik z poprzedniego generowania jest usuwany
        
        """
        super(GenratorPlikuTestowego, self).__init__()
        # czestotliwosc liter
        self.czest_liter = [] 
        self.suma = float(0)

        # usuwanie starego pliku
        if os.path.exists(PLIK_TRENINGOWY):
            os.remove(PLIK_TRENINGOWY)

    def obliczCzestotliwoscPliku(self, nazwa_pliku):
        """
        Oblicza częstoliwość liter dla danego pliku
        
        """
        with open(self.testFolder + nazwa_pliku) as f:
            zawartosc = f.read().lower()
            
            self.czest_liter = czestotliwosc(zawartosc)
            self.wyjscie()

    def wyjscie(self):
        """
        Wupisuje do pliku treningowego częstoliwość liter danego pliku

        """
        tekst = str()
        
        with open(PLIK_TRENINGOWY, 'a') as plik:
            for elem in self.czest_liter:
                tekst += str(elem) + ' '
        
            plik.write(tekst + '\n')

        self.czest_liter = []

    def podsumowanieTestu(self, tekst):
        """
        Wypisuje tekst podsumowujący - może być dowolny
        
        """
        with open(PLIK_TRENINGOWY, 'a') as plik:
            plik.write(tekst + '\n\n')
  
    def generuj(self, dir=testFolder):
        """
        Generuje plik testowy na podstawie folderu z plikami języków

        W efekcie generuje plik treningowy z częstoliwościami i pełnym
        podsumowaniem.
        
        """
        pliki_testowe = os.listdir(dir)
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
    """
    Generowanie pliku testowego bez gui
    
    """
    gen = GenratorPlikuTestowego()
    gen.generuj()