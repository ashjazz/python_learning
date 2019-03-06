# coding=UTF-8
# 博客上的多进程运用程序
import ctypes
import datetime
import os, random, time
import sys

from multiprocessing import Queue
from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing import Pool
from multiprocessing import Value


# print (sys.executable)
# os._exit(0)
class entry:
    def __init__(self, s: str, q: Queue):
        self.s = s
        self.q = q        

    def cutString(self):
        index = random.randint(0, len(self.s) - 4)
        time.sleep(1)
        i = random.randint(0, 2)
        return self.s[index: index + 2]

    def exec(self):
        substring = self.cutString()
        self.q.put(substring)
        return substring

    def display(self, s):
        global index
        index += 1
        print("callback ----> {} :\t{}".format(index-1, s))

    # 检测进程执行方法是否成功的回调函数
    def printSign(self, s):
        print (s)
        pass


if __name__ == '__main__':
    param = "0123456789abcdefghijklmnopqrstuvwxyz"
    index = 1
    # 通过Manager模块创建共享对象用于进程池的进程之间的通信
    manager = Manager()
    queue = manager.Queue()

    # 测试12个进程的进程池执行 doMatch() 函数30次需要的时间
    pool1 = Pool(12)
    start = datetime.datetime.now()
    for i in range(30):
        e = entry(param, queue)
        pool1.apply_async(e.exec, callback = e.display, error_callback = e.printSign)

    pool1.close()
    pool1.join()
    finish = datetime.datetime.now()
    tmp = []
    while not queue.empty():
        tmp.append(queue.get())
    print("12个进程的进程池执行结果:\n{}".format(tmp))
    print("12个进程的进程池执行花费的时间为：\t{}".format(finish - start))

    # 测试3组4个进程的进程池执行 doMatch() 函数30次需要的时间
    pool2 = Pool(4)
    pool3 = Pool(4)
    pool4 = Pool(4)
    pools = [pool2, pool3, pool4]
    index = 1

    start = datetime.datetime.now()
    for j in range(len(pools)):
        for i in range(10):
            e = entry(param, queue)
            pools[j].apply_async(e.exec, callback=e.display)

        pools[j].close()
    for j in range(len(pools)):
        pools[j].join()
    finish = datetime.datetime.now()
    print("3组4个进程的进程池执行花费的时间为：\t{}".format(finish - start))
    tmp = []
    while not queue.empty():
        tmp.append(queue.get())
    print("3组4个进程的进程池执行结果：\n{}".format(tmp))