# enconding: utf-8
from programas.libro import Libro


class Librero:
    lb = []

    def __int__(self, nombre, autor, editorial):
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial

    def muestra(self):
        for i in range(len(self.lb)):
            print("libro {} del autor {} editorial{}", format(self.nombre, self.autor, self.editorial))
