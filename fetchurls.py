import threading
import urllib3


class Fetchurls(threading.Thread):
    def __init__(self, urls, output, lock):
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.lock = lock

    def run(self):
        while self.urls:
            url = self.urls.pop()
            req = urllib3.PoolManager()
            try:
                r = req.request('GET', url)
            except:
                print("No se pudo completar, revise url")

            self.lock.acquire()
            print('c', self.name)
            self.output.write(r.data.decode('UTF-8'))
            print("write done by", self.name)
            print("lock realed by", self.name)
            self.lock.release()
