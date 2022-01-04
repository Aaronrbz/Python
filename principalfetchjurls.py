from fetchurls import *
import threading

urls1 = ['https://listado.mercadolibre.com.mx', 'https://www.pinterest.com.mx']
urls2 = ['https://listado.mercadolibre.com.mx', 'https://www.pinterest.com.mx']
lock = threading.Lock()
f = open('output.txt', 'w+')
t1 = Fetchurls(urls1, f, lock)
t2 = Fetchurls(urls2, f, lock)
t1.start()
t2.start()

