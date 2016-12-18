
from multiprocessing import Process
from time import sleep

def FI(i):
    for k in range(i):
        print("function", k)
        sleep(0.01)

def FI2(i):
    for k in range(i):
        print("function 2 ", k)
        sleep(0.01)

def main():
    l = 1000

    Process(target=FI, args=(l,)).start()
    Process(target=FI2, args=(l,)).start()

    for i in range (l):
        print ("main", i)
        sleep(0.01)
    # p1.join()
    # p2.join()


if __name__ == '__main__':
    main()