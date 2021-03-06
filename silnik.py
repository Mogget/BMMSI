# -*- coding: utf-8 -*-

import math
import random
#import string

from PyQt4.QtCore import QObject, pyqtSignal

from czest import czestotliwosc

random.seed(0)


def losuj(a, b):
    """ 
    funkcja losująca liczby wykorzystywana do
    uzupelnienia macierzy wag poczatkowych
    
    """
    return (b - a) * random.random() + a


def tworzMacierz(I, J, fill=0.0):
    """ Tworzy macierz polaczen """
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m

def sigmoid(x):
    """ fukcja sigmod """
    return math.tanh(x)


def dsigmoid(y):
    """ liczy blad kwadratowy """
    return 1.0 - y ** 2


class SSN(QObject):
    """
    Klasa Sztucznej Sieci Neuronowej
    uczącej się za pomocą algorymu propagacji wstecznej
    
        
    """
    
    tekst_na_log = pyqtSignal("QString", name="logEntry")
    

    def __init__(self, liczbaWarstw, liczbaNeuronow=[]):
        """ konstruktor, tworzac obiekt tworzymy siec """
        super(SSN, self).__init__()
        self.liczbaNeuronow = liczbaNeuronow
        self.liczbaNeuronow[0] += 1     # nie wiem czemu

        # lista z progami aktywacji dla wezla
        self.progAktywacji = []
        for neuron in self.liczbaNeuronow:
            self.progAktywacji.append([1.0] * neuron)

        # tworzenie wag
        self.wagi = []
        for licznik in range(len(self.liczbaNeuronow) - 1):
            self.wagi.append(tworzMacierz(self.liczbaNeuronow[licznik],\
                    self.liczbaNeuronow[licznik + 1]))

        # ustaw wartosci randomowe dla wag
        for neuron in range(len(self.liczbaNeuronow) - 1):
            for i in range(self.liczbaNeuronow[neuron]):
                for j in range(self.liczbaNeuronow[neuron + 1]):
                    self.wagi[neuron][i][j] = losuj(-0.2, 0.2)

        # ostatnia zmiana wag dla momentum
        self.zmianaWagi = []
        for licznik in range(len(self.liczbaNeuronow) - 1):
            self.zmianaWagi.append(tworzMacierz(self.liczbaNeuronow[licznik],\
                    self.liczbaNeuronow[licznik + 1]))


    def update(self, wejscie):
        """ zmienia wartość wyjść na podstawie wjeść """
        
        if len(wejscie) != self.liczbaNeuronow[0] - 1:
            raise ValueError('liczba wejsc pliku testowego jest zla')

        # ustawienie progu aktywacji wejscia
        for i in range(self.liczbaNeuronow[0] - 1):
            #self.ai[i] = sigmoid(inputs[i])
            self.progAktywacji[0][i] = wejscie[i]
            
        # prog aktywacji warstw dalszych
        for licznik in range(len(self.liczbaNeuronow) - 1):
            for j in range(self.liczbaNeuronow[licznik + 1]):
                sum = 0.0
                for i in range(self.liczbaNeuronow[licznik]):
                    sum = sum + self.progAktywacji[licznik][i] * self.wagi[licznik][i][j]
                self.progAktywacji[licznik + 1][j] = sigmoid(sum)

        return self.progAktywacji[-1][:]


    def backPropagate(self, cel, N, M):
        """
        wykonuje algortym wsteznej propragacji błędów 
        
        N - współczynnik uczenia
        M - współczynnik momentum
        
        """
        if len(cel) != self.liczbaNeuronow[-1]:
            raise ValueError('niepoprawna liczba wejsc w pliku testowym\
                    lub w tworzonej sieci')

        delta = []
        # obliczanie błędu dla wyjsc
        delta.append([0.0] * self.liczbaNeuronow[-1])
        for k in range(self.liczbaNeuronow[-1]):
            error = cel[k] - self.progAktywacji[-1][k]
            delta[0][k] = dsigmoid(self.progAktywacji[-1][k]) * error

        # obliczanie bledu dla warst ukrytych
        for licznik in range(len(self.liczbaNeuronow[1: -1])):
            delta.append([0.0] * self.liczbaNeuronow[-2 - licznik])
            for j in range(self.liczbaNeuronow[-2 - licznik]):
                error = 0.0
                for k in range(self.liczbaNeuronow[-1 - licznik]):
                    error = error + delta[-2][k] * self.wagi[-1 - licznik][j][k]
                delta[-1][j] = dsigmoid(self.progAktywacji[-2 - licznik][j]) * error

        # aktualizacja wag
        for licznik in range(len(self.liczbaNeuronow[: -1])):
            for j in range(self.liczbaNeuronow[-2 - licznik]):
                for k in range(self.liczbaNeuronow[-1 - licznik]):
                    change = delta[licznik][k] * self.progAktywacji[-2 - licznik][j]
                    self.wagi[-1 - licznik][j][k] = self.wagi[-1 - licznik][j][k] + N * change + M * self.zmianaWagi[-1 - licznik][j][k]
                    self.zmianaWagi[-1 - licznik][j][k] = change

        # obliczanie bledu sredniokwadratowego
        error = 0.0
        for k in range(len(cel)):
            error = error + 0.5 * (cel[k] - self.progAktywacji[-1][k]) ** 2
        return error
    

    def test(self, wzorzec):
        """
        Przprowadza pomiar dla zadanego wzorca
        
        """
        wynik = self.update(wzorzec)
        #print wzorzec, '->', wynik, '\n'
       
        self.tekst_na_log.emit( 'Angielski: ' + str(wynik[0]) )
        self.tekst_na_log.emit( 'Niemiecki: ' + str(wynik[1]) )
        self.tekst_na_log.emit( 'Polski:    ' + str(wynik[2]) )
        self.tekst_na_log.emit( 'Francuski: ' + str(wynik[3]) )
        return wynik


    def wagi(self):
        """
        Wyświetla wagi wejściowe i wyjściowe
        """
        print('Wagi wejsciowe:')
        for i in range(self.liczbaNeuronow[0]):
            print(self.wagi[0][i])
        print()
        print('Wagi wyjsciowe:')
        for j in range(self.liczbaNeuronow[-2]):
            print(self.wagi[-1][j])


    def train(self, wzorzec, liczbaEpok=1000, N=0.5, M=0.1, min_blad=0.3):
        """
        Trenuje SSN dla zadanego wzorca,
        przez zadaną liczbę epok lub do uzyskania 
        oczekiwanej wartości błędu.
        
         N: intensywność nauki
         M: współczynnik pędu (momentum)
        """
        indeks = 2
        testowy = []
        plik = open(wzorzec)
        try:
            plikTestowy = plik.readlines()
        finally:
            plik.close()

        # obrabia wczytane z pliku dane tekstowe
        while indeks < len(plikTestowy):
            testowy.append([float(lista) for lista in plikTestowy[indeks].split(' ')[:-1]])
            indeks += 1
            testowy.append([int(lista) for lista in plikTestowy[indeks].split(' ')[:-1]])
            indeks += 2

        # w petli uczy wszystkie dane testowe i zlicza bledy
        for i in range(liczbaEpok):
            error = 0.0
            for p in range(len(testowy))[::2]:
                try:
                    wejscie = testowy[p]
                    cel = testowy[p + 1]
                except:
                    pass
                self.update(wejscie)
                error = error + self.backPropagate(cel, N, M)

            if error <= min_blad:
                break
                
            # co 50 epok wyswietla blad
            if i % 50 == 0:
                self.tekst_na_log.emit( 'Epoka: \t%5d error: %-.5f' % (i, error) )
            if i == liczbaEpok-1:
                self.tekst_na_log.emit( 'Epoka: \t%5d error: %-.5f' % (i+1, error) )
            if i % 100 == 0:
                print 'Epoki\t%5d. error: %-.5f' % (i, error)
        #print wejscie

        # self.update(wzorzec[0][0])


def demo():
    """
    Uruchamia silnik SSN bez GUI
    """
    # Wersja demo silnika, bez GUI
    # Sieć z 4 warstawami
    # 25 - warswa wejściowa - czestoliwosc alfabetu lacinksiego
    # 2 x warstwa ukryta po 40 znakow
    # 4 neurony warstwy wyjsciowej 
    n = SSN(4, [25, 40, 40, 4])
    # plik treningowy
    n.train("test.txt")
    # Teksty testowe
    tekstDe = 'Ein neuer Renner der Fernsehindustrie heist "Big Brother". Es gengt nicht, da viele Menschen ihre eigene, oft traurige, Realitt verdrngen, indem sie mit bewundernswerter Disziplin die Schicksale der Serienhelden verfolgen. Nein. Die Massen ergtzen sich neuerdings an dem tristen Alltag einiger in einem Container eingeschlossenen Leute. Sie beobachten die neuen Kultfiguren beim Rasieren oder Zhneputzen, hren langweiligen Gesprchen zu und warten auf einen Knller, eine Sensation.'
    tekstEn = 'If you take a look at the average day of the average family you would be surprised by the amount of time they spend watching TV. Films, quizes, news, soap operas, shows and sport - all in one in a little box in your home that is waiting for you to press the button. There is no doubt about it, TV attracts its viewers in every possible'
    tekstPl = 'ąęźćńBrytyjski aktor znany z roli Remisa Lupina z filmowej serii przygd Harryego Pottera. David Thewlis wcieli si w posta dilera informacji, znanego jako The Frog. Bohater zaczerpnie swj pseudonim po tym, jak zatruje wod w budynku Kremla przy pomocy egzotycznej aby z Amazonii. W kontynuacji filmu z 2010 roku, ujrzymy znw emerytowanych agentw CIA, w osobach Brucea Willisa, Helen Mirren i Johna Malkoicha, ktrzy uyj swojego dowiadczenia, aby ciga bandytw na terenie Europy. Swj udzia w "Red 2" potwierdzili take Catherine Zeta-Jones i Anthony Hopkins.'
    tekstFr = 'Bien sur, dit le renard. Tu nes encore pour moi quun petit garon tout semblable a cent mille petits garons. Et je nai pas besoin de toi. Et tu nas pas besoin de moi non plus. Je ne suis pour toi quun renard semblable a cent mille renards. Mais, si tu mapprioises, nous aurons besoin lun de lutre. Tu seras pour moi unique au monde. Je serai pour toi unique au monde'
    # Sprawdzenie języka    
    n.test(czestotliwosc(tekstEn))
    n.test(czestotliwosc(tekstDe))
    n.test(czestotliwosc(tekstPl))
    n.test(czestotliwosc(tekstFr))


if __name__ == '__main__':
    demo()
