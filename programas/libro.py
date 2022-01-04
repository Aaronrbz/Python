# enconding: utf-8
class Libro:
    lb = []

    def __int__(self, nombre, autor, editorial):
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial

    def insertarlibro(self, nombre, autor="anonimo", editorial="desconocida"):
        self.lb.append(nombre)
        self.lb.append(autor)
        self.lb.append(editorial)


        #self.lb.append(nombre)+self.lb.append(autor)+self.append(editorial)
       # self.lb.append(Libro.insertalibro(nombre, autor, editorial))
