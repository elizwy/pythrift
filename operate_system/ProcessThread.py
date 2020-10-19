import threading
from operate_system import Task


class ProcessThread(threading.Thread):

    def __init__(self, task_queue, *args, **kwargs):
        threading.Thread.__init__(*args, **kwargs)
        self.dismiss_flag = threading.Event();
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while True:
            if self.dismiss_flag.isSet():
                break
            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            result = task.callable(*task.args, **task.kwargs)

    def dismiss(self):
        self.dismiss_flag.set()


    def stop(self):
        pass
