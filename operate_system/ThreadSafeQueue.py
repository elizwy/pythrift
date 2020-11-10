import threading
import time


class ThreadSafeQueueException(Exception):
    pass


class ThreadSafeQueue(object):

    def __init__(self, maxSize=0):
        self.maxSize = maxSize
        self.queue = []
        self.lock = threading.Lock()
        self.condition = threading.Condition()

    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    def get(self, index):
        self.lock.acquire()
        item = self.queue[index]
        self.lock.release()
        return item

    def put(self, item):
        if self.size() == self.maxSize:
            return ThreadSafeQueueException()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()
        pass

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    def pop(self, block=False, timeout=0):
        if self.size() == 0:
            if block:
                self.condition.acquire()
                self.condition.wait(timeout)
                self.condition.release()
            else:
                return None
        if self.size() == 0:
            return None
        self.lock.acquire()
        item = self.queue.pop()
        self.lock.release()
        return item


if __name__ == '__main__':
    queue = ThreadSafeQueue(10)


    def producer():
        while True:
            queue.put(1)
            time.sleep(3)


    def consumer():
        while True:
            item = queue.pop(block=True, timeout=2)
            print("get item from queue:%d", item)
            time.sleep(3)


    thread1 = threading.Thread(target=producer)
    thread2 = threading.Thread(target=consumer)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
