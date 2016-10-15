import threading


class Interval(object):

    def __init__(self, func, sec):

        def run_interval():
            self.t = threading.Timer(sec, func_wrapper)
            self.t.start()

        def func_wrapper():
            func()
            run_interval()

        run_interval()

    def cancel(self):
        self.t.cancel()


if __name__ == '__main__':

    def log():
        print('log')
    i = Interval(log, 1)
