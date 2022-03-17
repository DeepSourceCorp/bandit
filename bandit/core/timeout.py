import signal


class BanditTimeoutError(Exception):
    pass


def signal_handler(signum, frame):
    raise BanditTimeoutError()


def timeout(func, *args, seconds=1, default=None):
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        func(*args)
    except BanditTimeoutError:
        return True
    finally:
        signal.alarm(0)

    return False
