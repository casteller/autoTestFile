from random import randint
from time import ctime, sleep
import threading

#先定义 一把锁
lock=threading.Lock()
def cook(cooker, cost_time):
    lock.acquire()#进厨房锁门
    for i in range(2):
        print("%s正在用厨房-------%s" % (cooker,ctime()))
        sleep(cost_time)
    print("%s用完厨房-------%s" % (cooker,ctime()))
    lock.release()#出厨房开门


if __name__ == '__main__':
    cookers=['小张','小李','小王']
    threads = []
    for m in cookers:
        t = threading.Thread(target=cook, args=(m, randint(1,4)))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("做好了！！！%s" % ctime())