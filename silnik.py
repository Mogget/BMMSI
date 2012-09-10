# -*- coding: utf-8 -*-

import math
import random
#import string

from const import obslugiwane_litery
from czest import czestotliwosc

random.seed(0)


def losuj(a, b):
    return (b - a) * random.random() + a


# TODO: do spolszczenia
# tworzy macierz polaczen
def tworzMacierz(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m

def sigmoid(x):
    return math.tanh(x)


def dsigmoid(y):
    return 1.0 - y ** 2


class SSN(object):
    """docstring for SiecNeuronowa"""
    

    def __init__(self, liczbaWarstw, liczbaNeuronow=[]):
        super(SSN, self).__init__()
        self.liczbaNeuronow = liczbaNeuronow
        self.liczbaNeuronow[0] += 1     # nie wiem czemu

        # prog aktywacji dla wezla
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
                    #TODO: inne losowanie jest w bpnn ale to i tak nie powinno miec zwiazku
                    self.wagi[neuron][i][j] = losuj(-0.2, 0.2)

        # last change in weights for momentum
        self.zmianaWagi = []
        for licznik in range(len(self.liczbaNeuronow) - 1):
            self.zmianaWagi.append(tworzMacierz(self.liczbaNeuronow[licznik],\
                    self.liczbaNeuronow[licznik + 1]))


    def update(self, wejscie):
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
        if len(cel) != self.liczbaNeuronow[-1]:
            raise ValueError('wrong number of target values')

        delta = []
        # calculate error terms for output
        delta.append([0.0] * self.liczbaNeuronow[-1])
        for k in range(self.liczbaNeuronow[-1]):
            error = cel[k] - self.progAktywacji[-1][k]
            delta[0][k] = dsigmoid(self.progAktywacji[-1][k]) * error

        # calculate error terms for hidden
        for licznik in range(len(self.liczbaNeuronow[1: -1])):
            delta.append([0.0] * self.liczbaNeuronow[-2 - licznik])
            for j in range(self.liczbaNeuronow[-2 - licznik]):
                error = 0.0
                for k in range(self.liczbaNeuronow[-1 - licznik]):
                    error = error + delta[-2][k] * self.wagi[-1 - licznik][j][k]
                delta[-1][j] = dsigmoid(self.progAktywacji[-2 - licznik][j]) * error

        # update output weights
        for licznik in range(len(self.liczbaNeuronow[: -1])):
            for j in range(self.liczbaNeuronow[-2 - licznik]):
                for k in range(self.liczbaNeuronow[-1 - licznik]):
                    change = delta[licznik][k] * self.progAktywacji[-2 - licznik][j]
                    self.wagi[-1 - licznik][j][k] = self.wagi[-1 - licznik][j][k] + N * change + M * self.zmianaWagi[-1 - licznik][j][k]
                    self.zmianaWagi[-1 - licznik][j][k] = change
                    #print N*change, M*self.co[j][k]

        # calculate error
        error = 0.0
        for k in range(len(cel)):
            error = error + 0.5 * (cel[k] - self.progAktywacji[-1][k]) ** 2
        return error
    

    def test(self, wzorzec):
        print wzorzec, '->', self.update(wzorzec), '\n'
        return self.update(wzorzec)


    def weights(self):
        print('Input weights:')
        for i in range(self.liczbaNeuronow[0]):
            print(self.wagi[0][i])
        print()
        print('Output weights:')
        for j in range(self.liczbaNeuronow[-2]):
            print(self.wagi[-1][j])


    def train(self, wzorzec, liczbaEpok=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        print "maksymalna liczba Epok \t", liczbaEpok
        indeks = 2
        testowy = []
        plik = open(wzorzec)
        try:
            plikTestowy = plik.readlines()
        finally:
            plik.close()

        while indeks < len(plikTestowy):
            testowy.append([float(lista) for lista in plikTestowy[indeks].split(' ')[:-1]])
            indeks += 1
            testowy.append([int(lista) for lista in plikTestowy[indeks].split(' ')[:-1]])
            indeks += 2

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
            if i % 100 == 0:
                print 'Epoki\t%5d. error: %-.5f' % (i, error)
        #print wejscie

        # self.update(wzorzec[0][0])


def demo():

    # create a network with two input, two hidden, and one output nodes
    n = SSN(4, [25, 40, 40, 4])
    # train it with some patterns
    n.train("test.txt")
    # test it
#TODO: dzialaja tylko znaki ascii ;/
    tekstDe = 'Ein neuer Renner der Fernsehindustrie heist "Big Brother". Es gengt nicht, da viele Menschen ihre eigene, oft traurige, Realitt verdrngen, indem sie mit bewundernswerter Disziplin die Schicksale der Serienhelden verfolgen. Nein. Die Massen ergtzen sich neuerdings an dem tristen Alltag einiger in einem Container eingeschlossenen Leute. Sie beobachten die neuen Kultfiguren beim Rasieren oder Zhneputzen, hren langweiligen Gesprchen zu und warten auf einen Knller, eine Sensation.'
    tekstEn = 'If you take a look at the average day of the average family you would be surprised by the amount of time they spend watching TV. Films, quizes, news, soap operas, shows and sport - all in one in a little box in your home that is waiting for you to press the button. There is no doubt about it, TV attracts its viewers in every possible'
    tekstPl = 'ąęźćńBrytyjski aktor znany z roli Remisa Lupina z filmowej serii przygd Harryego Pottera. David Thewlis wcieli si w posta dilera informacji, znanego jako The Frog. Bohater zaczerpnie swj pseudonim po tym, jak zatruje wod w budynku Kremla przy pomocy egzotycznej aby z Amazonii. W kontynuacji filmu z 2010 roku, ujrzymy znw emerytowanych agentw CIA, w osobach Brucea Willisa, Helen Mirren i Johna Malkoicha, ktrzy uyj swojego dowiadczenia, aby ciga bandytw na terenie Europy. Swj udzia w "Red 2" potwierdzili take Catherine Zeta-Jones i Anthony Hopkins.'
    tekstFr = 'Bien sur, dit le renard. Tu nes encore pour moi quun petit garon tout semblable a cent mille petits garons. Et je nai pas besoin de toi. Et tu nas pas besoin de moi non plus. Je ne suis pour toi quun renard semblable a cent mille renards. Mais, si tu mapprioises, nous aurons besoin lun de lutre. Tu seras pour moi unique au monde. Je serai pour toi unique au monde'
    n.test(czestotliwosc(tekstEn))
    n.test(czestotliwosc(tekstDe))
    n.test(czestotliwosc(tekstPl))
    n.test(czestotliwosc(tekstFr))


if __name__ == '__main__':
    demo()
