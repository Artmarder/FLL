import micropython
from _thread import start_new_thread
from MyDivece import motor

@micropython.native
def thread(func):
    def wrapper(*args, **kwargs):
        start_new_thread(func, args, kwargs)
    return wrapper

class Timer:
    def __init__(self):
        self.Stime = _time()
        self.Ptime = _time()

    @micropython.native
    def get(self):
        return _time() - self.Stime

    @micropython.native
    def reset(self):
        self.Stime = _time()

    @micropython.native
    def pause(self):
        self.Ptime = _time()
        
    @micropython.native
    def play(self):
        self.Stime += _time() - Ptime
        self.Ptime = None

    def calcDistance():
        correct_postionA = get_angel_postioin_A()
        correct_postionB = get_angel_postioin_B()
        calc_distance =correct_postionB  + correct_postionA  / 360 / 2 * 17.5



