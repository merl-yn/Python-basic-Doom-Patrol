import time
from datetime import datetime


class Logger:
    logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self):
        log = f'{self.func.__name__} with was executed at {datetime.now()}\n'
        print(log)
        with open(self.logfile, 'a') as file:
            file.write(log)


@Logger
def my_func():
    """
    This is my func
    """
    return f"{my_func().__name__} is running"


my_func()
