#!/usr/bin/env python

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


def czestotliwosc(tekst):
    wynik = []
    suma = 0
    fLitera = []
    litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
                'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'q', 'x', 'y', 'z']
    for wartosc in litery:
        suma += float(tekst.count(wartosc))
        fLitera.append(float(tekst.count(wartosc)))

    for wartosc in fLitera:
        wynik.append(wartosc / suma)

    return wynik


def sigmoid(x):
    return math.tanh(x)


def dsigmoid(y):
    return 1.0 - y ** 2


class SiecNeuronowa(object):
    """docstring for SiecNeuronowa"""
    def __init__(self, liczbaWarstw, liczbaNeuronow=[]):
        super(SiecNeuronowa, self).__init__()
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
        if len(wejscie) != len(self.liczbaNeuronow) - 1:
            raise ValueError('liczba wejsc pliku testowego jest zla')

        # ustawienie progu aktywacji wejscia
        for i in range(self.liczbaNeuronow[0] - 1):
            #self.ai[i] = sigmoid(inputs[i])
            self.progAktywacji[0][i] = wejscie[i]
        # prog aktywacji warst dalszych
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
        for w in wzorzec:
            print(w[0], '->', self.update(w[0]))

    def weights(self):
        print('Input weights:')
        for i in range(self.liczbaNeuronow[0]):
            print(self.wagi[0][i])
        print()
        print('Output weights:')
        for j in range(self.liczbaNeuronow[-2]):
            print(self.wagi[-1][j])

    def train(self, wzorzec, liczbaIteracji=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(liczbaIteracji):
            error = 0.0
            for p in wzorzec:
                wejscie = p[0]
                cel = p[1]
                self.update(wejscie)
                error = error + self.backPropagate(cel, N, M)
            if i % 100 == 0:
                print('error %-.5f' % error)

        # self.update(wzorzec[0][0])


def demo():
    # Teach network XOR function
    pat = [
        [[0, 0], [0]],
        [[0, 1], [1]],
        [[1, 0], [1]],
        [[1, 1], [0]]
    ]

    # create a network with two input, two hidden, and one output nodes
    n = SiecNeuronowa(3, [2, 2, 1])
    # train it with some patterns
    n.train(pat)
    # test it
    n.test(pat)


if __name__ == '__main__':
    demo()
