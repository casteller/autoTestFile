from random import randint
from time import ctime, sleep
import threading

# 初始账户

account = 50

#获取锁对象
lock=threading.Lock()

#抢红包
def add(amount):
    global account
    for i in range(1000000):
        # lock.acquire()#锁上
        with lock:
            account += amount
        # lock.release()#释放锁，解锁，开锁

#发红包
def div(amount):
    global account
    for i in range(1000000):
        # lock.acquire()  # 锁上
        with lock:
            account -= amount
        # lock.release()  # 释放锁，解锁，开锁


t1 = threading.Thread(target=add,args=(5,))
t2 = threading.Thread(target=div,args=(5,))

t1.start()
t2.start()
t1.join()
t2.join()

print('余额还剩%d元'%account)