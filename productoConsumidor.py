import threading
from random import randint
import time


class Productor(threading.Thread):
    def __init__(self, enteros, condicion):
        threading.Thread.__init__(self)
        self.enteros = enteros
        self.condicion = condicion


def run(self):
    while True:
        entero = randint(0, 256)
        self.condicion.acquire()
        print("Condicion adquirida por:", self.name)
        self.entero.appened(entero)
        print("{} agregado a la lista {}".format(entero, entero))
        print("condicion notifiada por :", self.name)
        self.name.notify()
        print("condicion liberada por: ", self.name)
        self.condicion.release()
        time.sleep(1)


class consumidor(threading.Thread):
    def __init__(self, enteros, condicion):
        threading.Thread.__init__(self)
        self.enteros = enteros
        self.condicion = condicion


def run(self):
    while True:
        self.condicion.acquire()
        print("Condicion adquirida por", self.name)
        while True:
            if self.enteros:
                entero = self.enteros.pop()
                print("{} adquirido de la lista {}".format(entero, entero))
                break
            print("condicion en espera", self.name)
            self.condicion.wait()
        print("condicion liberada por", self.name)
        self.condicion.release()
