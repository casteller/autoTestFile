'''生产者与消费者'''
from time import ctime, sleep
from queue import Queue
from threading import Thread

# 老板做包子
def producer(out_q):
    while True:
        # 一秒钟做一个包子
        if out_q.full():
            print('盘子满了！！！！')
        else:
            out_q.put('包子')
            print('做包子%s'%ctime())
        sleep(1)

# 客人吃包子
def consumer(in_q):
    while True:
        # 2秒种吃一个包子
        if in_q.empty():
            print('包子没了！！！！！')
        else:
            data = in_q.get()
            print('吃%s! %s'%(data,ctime()))
        sleep(3)


# 建一个做包子的线程和吃包子的线程，包子做好，直接放到盘子里面，客人自己拿
panzi = Queue(5)#盘子
boss = Thread(target=producer, args=(panzi,))
c1 = Thread(target=consumer, args=(panzi,))
c2 = Thread(target=consumer, args=(panzi,))

boss.start()
c1.start()
c2.start()