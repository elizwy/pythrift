import uuid


class Task:
    def __init__(self, func, *args, **kwargs):
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs
        self.callable = func

    def __str__(self):
        return "task id: " + str(self.id)


def my_function():
    print("this is a test task")


if __name__ == "__main__":
    task = Task(func=my_function())
    print(task)
