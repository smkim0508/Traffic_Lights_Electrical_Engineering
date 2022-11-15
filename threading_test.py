from threading import Thread
import time 

def func1():
    print("2")
    time.sleep(1)
    print("5")

def func2():
    print("3")
    time.sleep(1)
    print("6")


if __name__ == '__main__':
    print("1")
    a = Thread(target = func1)
    b = Thread(target = func2)
    a.start()
    b.start()
    print("4")