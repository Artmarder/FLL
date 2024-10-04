from _thread import start_new_thread


def thread(func):
    """
    This decorator return the given function as a thread.

    Parameters: func: Function
    Returns: func: Thread
    """
    def wrapper(*args, **kwargs):
        start_new_thread(func, args, kwargs)
    return wrapper


