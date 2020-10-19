import psutil as psutil

from operate_system.ThreadSafeQueue import ThreadSafeQueue


class ThreadPool():

    def __init__(self,size):
        if not size:
            size=psutil.cpu_count*2
        self.pool=ThreadSafeQueue(size)


    def size(self):
        pass


    def start(self):
        pass

    def join(self):
        pass

    def put(self):
        pass

    def batch_put(self):
        pass