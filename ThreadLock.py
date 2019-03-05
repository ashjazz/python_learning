# coding=UTF-8
import threading
import time
num = 0

def myRun(lock):
    global num
    time.sleep(1)
    # 尝试获取互斥锁，将锁置为locked状态，当blocking = True时会阻塞当前线程
    if lock.acquire():
        num += 1
        pass
        # threading.currentThread().setName('Thread-{}'.format(num))
    print ('I am thread: {}, set counter: {}'.format(threading.currentThread().getName(), num))
    # 释放互斥锁，将锁状态更改为unlocked，但如果对一个未锁定的锁使用该方法时会抛出异常
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock() # 共用一个锁对象，100个线程会互相阻塞发生锁等待，资源的完整性没有被破坏
    for i in range(100):
        # lock = threading.Lock() #每次循环都新建一个锁对象，则线程之间不会互相阻塞，资源的完整性破坏
        # 线程会出现资源抢占现象
        myThread = threading.Thread(target = myRun, args = (lock, ))
        myThread.setName('Thread-{}'.format(i))
        myThread.start()