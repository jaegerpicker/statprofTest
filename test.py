import statprof
import time


def next_func():
    for x in range(0, 10000):
        y = x * 2
        print y


def expensive_function():
    time.sleep(0.05)
    next_func()


def my_questionable_function():
    for i in range(0, 1000):
        print "test {0}".format(i)
        expensive_function()


statprof.start()
try:
    my_questionable_function()
finally:
    statprof.stop()
    statprof.display()
