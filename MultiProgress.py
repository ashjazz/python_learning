# coding=UTF-8
# multiprocessing是跨平台的多进程模块 用Process类来代表进程对象
# multiprocessing模块提供了进程间通信的方式，其中queue就是一种
from multiprocessing import Process, Queue
import os, time, random

# 向queue中写数据方法
def writeWork(queue):
    print ('Process1 is running ...')
    for letter in ['A', 'B', 'C']:
        print ('Process1 is writing %s to queue' % (letter))
        queue.put(letter)
        time.sleep(random.random())
    # if queue.full():
    #     print ('queue is full ...')

# 从queue中获取数据的方法
def readWork(queue):
    print ('Process2 is running ...')
    # 如果改成下列方式，则会因为进程2开始的时候进程1并没有及时向queue中写入数据而退出循环
    # 或者因为进程2从queue中取走了数据而进程1还没来得及向queue中写入下一个数据退出循环
    # while not queue.empty():
    #     letter = queue.get(True)
    #     print ('Process2 gets the word %s from queue' % (letter))
    #     time.sleep(random.random())
    while True:
        letter = queue.get(True)
        print ('Process2 gets the word %s from queue' % (letter))
        time.sleep(random.random())

if __name__ == '__main__':
    queue = Queue()
    # 将通信queue对象作为参数传入对应方法
    process1 = Process(target = writeWork, args = (queue, ))
    # process2 = Process(target = readWork, args = (queue, ))
    process1.start()
    # process2.start()
    process1.join()
    # 因为进程2是死循环，所以强制终止
    # process2.terminate()
    print ('END...')