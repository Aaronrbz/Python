class Archivo:
    def __init__(self, nombre):
        try:
            self.f = open(nombre, 'r')
            self.nombre = nombre
        except:
            print("No se puede abrir el archivo")
            exit()

    def muestra(self):
        for linea in self.f:
            print("{:3}:{}", format(linea), end="")
        self.f.seek(0)

    def cuentaVocales(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("aeiouàèììòù"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaConsonates(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("bcdfghjklmnpqrstvwxyz"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaSisgnosPuntuacion(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set(".,;:¡!¿?"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaEspacios(s):
        contador = 0
        for i in range(len(s)):
            if chr(32) == i:
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaPalabras(s):
        f = open(s, "r")
        text = f.readlines()
        f.close()
        cont = 0
        for lines in text:
            found = s.findall("([a-z\']+)", lines.strip(), s.I)
            if found:
                cont += len(found)
        if cont > 1:
            return "El archivo tiene %s palabras" % cont
            sel.f.seek(0)
        elif cont == 0:
            return "El archivo esta vacio"
            sel.f.seek(0)
        else:
            return "El archivo tiene %s palabra" % cont
            sel.f.seek(0)

    def cuentaLineas(s):
        print(len(s.readlines()))

    def cuentaMayusculas(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("QWERTYUIOPLKJHGFDSAZXCVBNM"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaMinuscula(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("qwertyuiopñlkjhgfdsazxcvbnm"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def copiaArchivo(origen="", destino=""):
        shutil.copyfile(origen, destino)

    def convierteMayuscula(s):
        f = open(s, "w")
        text = f.readlines()
        f.close()
        for i in range(len(s)):
            s[i] = s.upper()
        s.muestra(s)

    def convierteMinuscula(s):
        f = open(s, "w")
        text = f.readlines()
        f.close()
        for i in range(len(s)):
            s[i] = s.lower()
        s.muestra(s)

    def muestraHx(self):
        for linea in self.f:
            print(linea, linea.encode('hex'))
        self.f.seek(0)


import shutil
from sys import exit


class Archivo:
    def __init__(self, nombre):
        try:
            self.f = open(nombre, 'r')
            self.nombre = nombre
        except:
            print("No se puede abrir el archivo")
            exit()

    def muestra(self):
        for linea in self.f:
            print("{:3}:{}", format(linea), end="")
        self.f.seek(0)

    def cuentaVocales(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("aeiouàèììòù"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaConsonates(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("bcdfghjklmnpqrstvwxyz"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaSisgnosPuntuacion(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set(".,;:¡!¿?"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaEspacios(s):
        contador = 0
        for i in range(len(s)):
            if chr(32) == i:
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaPalabras(s):
        f = open(s, "r")
        text = f.readlines()
        f.close()
        cont = 0
        for lines in text:
            found = s.findall("([a-z\']+)", lines.strip(), s.I)
            if found:
                cont += len(found)
        if cont > 1:
            return "El archivo tiene %s palabras" % cont
            sel.f.seek(0)
        elif cont == 0:
            return "El archivo esta vacio"
            sel.f.seek(0)
        else:
            return "El archivo tiene %s palabra" % cont
            sel.f.seek(0)

    def cuentaLineas(s):
        print(len(s.readlines()))

    def cuentaMayusculas(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("QWERTYUIOPLKJHGFDSAZXCVBNM"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def cuentaMinuscula(s):
        contador = 0
        for i in range(len(s)):
            if s[i] in set("qwertyuiopñlkjhgfdsazxcvbnm"):
                contador += 1
        return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        sel.f.seek(0)
        return contador

    def copiaArchivo(origen="", destino=""):
        shutil.copyfile(origen, destino)

    def convierteMayuscula(s):
        f = open(s, "w")
        text = f.readlines()
        f.close()
        for i in range(len(s)):
            s[i] = s.upper()
        s.muestra(s)

    def convierteMinuscula(s):
        f = open(s, "w")
        text = f.readlines()
        f.close()
        for i in range(len(s)):
            s[i] = s.lower()
        s.muestra(s)

    def muestraHx(self):
        for linea in self.f:
            print(linea, linea.encode('hex'))
        self.f.seek(0)


s = 'clases3.txt'
archivo = Archivo(s)
archivo.cuentaVocales()
archivo.cuentaConsonates()
archivo.cuentaSisgnosPuntuacion()
archivo.cuentaEspacios()
archivo.cuentaPalabras(s)
archivo.cuentaLineas(s)
archivo.convierteMayuscula(s)
archivo.convierteMinuscula(s)
archivo.muestraHx(s)
