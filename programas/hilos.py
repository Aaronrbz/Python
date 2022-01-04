import time
from concurrent.futures import thread


class Mythread(thread.Thread):
    def __init__(self, i):
        self.h = i

    def run(self):
        time.delay(50)
        print("Hilo: ", self.h)


thread1 = Mythread(1)
thread2 = Mythread(2)
thread3 = Mythread(3)
thread1.start()
thread2.start()
thread3.start()
