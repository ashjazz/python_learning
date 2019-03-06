# coding=UTF-8

import threading
import os, time, random
import queue

is_product = True

class Producer(threading.Thread):
    def __init__(self, name = None, queue = None):
        threading.Thread.__init__(self, name = name)
        self.queue = queue

    def run(self):
        while True:
            num = random.randint(0, 10000)
            # 获取队列长度
            queue_size = self.queue.qsize()
            if queue_size < 7:
                is_product = True
                self.queue.put(num)
                print ('put the num {} into queue, the left num is {}'.format(num, self.queue.qsize()))
                time.sleep(1)
            elif queue_size >20:
                is_product = False
            else:
                if is_product == True:
                    self.queue.put(num)
                    print ('put the num {} into queue, the left num is {}'.format(num, self.queue.qsize()))
                    time.sleep(1)
                else:
                    pass

# 从队列中取出奇数
class ConsumerOdd(threading.Thread):
    def __init__(self, name = None, queue = None):
        threading.Thread.__init__(self, name = name)
        self.queue = queue

    def run(self):
        while True:
            queue_size = self.queue.qsize()
            if queue_size < 7:
                pass
            else:
                num = self.queue.get(False)
                if num % 2 == 1:
                    print ('get a odd num {} from queue, the left num is {}'.format(num, self.queue.qsize()))
                else:
                    self.queue.put(num)
                time.sleep(2)

# 从队列中取出偶数
class ConsumerEven(threading.Thread):
    def __init__(self, name = None, queue = None):
        threading.Thread.__init__(self, name = name)
        self.queue = queue

    def run(self):
        while True:
            queue_size = self.queue.qsize()
            if queue_size < 7:
                pass
            else:
                num = self.queue.get(False)
                if num % 2 == 0:
                    print ('get a even num {} from queue, the left num is {}'.format(num, self.queue.qsize()))
                else:
                    self.queue.put(num)
                time.sleep(2)

if __name__ == '__main__':
    queue = queue.Queue()
    producer = Producer('Producer', queue)
    consumerOdd = ConsumerOdd('consumerOdd', queue)
    consumerEven = ConsumerEven('consumerEven', queue)
    producer.start()
    consumerOdd.start()
    consumerEven.start()
    producer.join()
    consumerOdd.join()
    consumerEven.join()


