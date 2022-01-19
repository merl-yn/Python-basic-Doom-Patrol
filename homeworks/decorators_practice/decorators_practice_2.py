import time
from datetime import datetime


class Logger:
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log = f'{func.__name__} with was executed at {datetime.now()}\n'
        print(log)
        with open(self.logfile, 'a') as file:
            file.write(log)


@Logger()
def my_func():
    """
    This is my func
    """
    print(f"{my_func().__name__} is running")


logger = Logger()
