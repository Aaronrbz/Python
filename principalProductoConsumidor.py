import productoConsumidor
import threading

enteros = []
condicion = threading.Condition()
t1 = productoConsumidor.Productor(enteros, condicion)
t2 = productoConsumidor.consumidor(enteros, condicion)
t1.start()
t2.start()
