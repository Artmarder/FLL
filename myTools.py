import micropython
from _thread import start_new_thread
from time import time

def mean():
    print('hello world !')

class Timer:
    def __init__(self):
        self.start_time = time()
        self.pause_time = None

    def get_elapsed_time(self):
        """Returns elapsed time in seconds."""
        if self.pause_time is None:
            return time() - self.start_time
        else:
            return self.pause_time - self.start_time

    def reset(self):
        self.start_time = time()
        self.pause_time = None

    def pause(self):
        self.pause_time = time()

    def resume(self):
        if self.pause_time is not None:
            elapsed = time() - self.pause_time
            self.start_time += elapsed
            self.pause_time = None


