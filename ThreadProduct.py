# coding=UTF-8

import threading
import os, time

left_num = 500
con = threading.Condition()

class Producer(threading.Thread):
    """生产者"""
    def __init__(self, target = None, name = None, args = (), kwargs = None):
        threading.Thread.__init__(self, target = target, name = name, args = args, kwargs = kwargs)

    def run(self):
        global left_num
        is_product = True
        while True:
            if con.acquire():
                if left_num > 5000:
                    is_product = False
                    # 不满足生产条件，由条件变量暂时挂起
                    con.wait()
                elif left_num < 1000:
                    left_num += 200
                    is_product = True
                    print ('{} produce 200, left_num is {}'.format(self.name, left_num))
                    # 唤醒被条件变量挂起的消费者
                    con.notify()
                else :
                    if is_product == True:
                        left_num += 200
                        print ('{} produce 200, left_num is {}'.format(self.name, left_num))
                        # 唤醒被条件变量挂起的消费者
                        con.notify()
                    else:
                        pass
                        con.wait()
                con.release()
                time.sleep(1)

class Consumer(threading.Thread):
    """消费者"""
    def __init__(self, target = None, name = None, args = (), kwargs = None):
        threading.Thread.__init__(self, target = target, name = name, args = args, kwargs = kwargs)

    def run(self):
        global left_num
        while True:
            if con.acquire():
                if left_num < 800:
                    pass
                    con.wait()
                else:
                    left_num -= 100
                    print ('{} consume 100, left_num is {}'.format(self.name, left_num))
                    con.notify()
                con.release()
                time.sleep(1)

def test():
    for i in range(1):
        p = Producer()
        p.start()
    for i in range(1):
        c = Consumer()
        c.start()
if __name__ == '__main__':
    test()

