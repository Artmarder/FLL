import micropython
from _thread import start_new_thread
from MyDivece import motor  # Assuming this is the correct import

def calc_distance(angle_a, angle_b):
    """Calculates distance based on given angles."""
    distance = angle_b + angle_a / 360 / 2 * 17.5
    return distance

class Timer:
    def __init__(self):
        self.start_time = _time()
        self.pause_time = None

    def get_elapsed_time(self):
        """Returns elapsed time in seconds."""
        if self.pause_time is None:
            return _time() - self.start_time
        else:
            return self.pause_time - self.start_time

    def reset(self):
        self.start_time = _time()
        self.pause_time = None

    def pause(self):
        self.pause_time = _time()

    def resume(self):
        if self.pause_time is not None:
            elapsed = _time() - self.pause_time
            self.start_time += elapsed
            self.pause_time = None


