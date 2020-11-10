import psutil as psutil

from operate_system.ProcessThread import ProcessThread
from operate_system.Task import Task
from operate_system.ThreadSafeQueue import ThreadSafeQueue


class TaskTypeErrorException(object):
    pass


class ThreadPool():

    def __init__(self, size=0):
        if not size:
            size = psutil.cpu_count() * 2
        self.pool = ThreadSafeQueue(size)
        self.task_queue=ThreadSafeQueue()
        for i in range(size):
            self.pool.put(ProcessThread(self.task_queue))

    def size(self):
        return self.pool.size();

    def start(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.start()

    def join(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.stop
        while self.pool.size():
            thread = self.pool.pop()
            thread.join()

    def put(self,item):
        if not isinstance(item,Task):
            raise TaskTypeErrorException()
        self.task_queue.put(item)

    def batch_put(self,item_list):
        if not isinstance(item_list,list):
            item_list=list(item_list)
        for item in item_list:
            self.put(item)
