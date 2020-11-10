import time

from operate_system import Task, ThreadPool


class SimpleTask(Task.Task):
    def __init__(self, callable):
        super(SimpleTask, self).__init__(callable)


def process():
    print("This is a simpleTest callable function")
    time.sleep(1)


def test():
    test_pool = ThreadPool.ThreadPool(None)
    test_pool.start()

    for i in range(10):
        simple_task = SimpleTask(process())
        test_pool.put(simple_task)
    pass


if __name__ == '__main__':
    test()
