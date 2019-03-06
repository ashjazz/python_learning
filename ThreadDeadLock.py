# coding=UTF-8
import threading
import os, time

# 创建两个线程，两个互斥锁对象，模拟死锁场景

def setThread1DeadLock(lock1, lock2):
    lock2.acquire()
    print ('thread1 is running')
    time.sleep(1)
    # 请求锁1，但此时锁1正在被线程2持有
    # 设置锁等待的最长时间为2秒，当2秒内没有获取到对应的锁资源时返回false，同时取消线程的阻塞
    if (lock1.acquire(timeout = 2)):
        lock2.release()
        print ('lock1 is locked, lock2 is released')
    else:
        print('acquire lock2 failed')
        lock2.release()

def setThread2DeadLock(lock1, lock2):
    lock1.acquire()
    print ('thread2 is running')
    time.sleep(1)
    # 请求锁2，但是锁2正在被线程1持有
    # 设置锁等待的最长时间为2秒，当2秒内没有获取到对应的锁资源时返回false，同时取消线程的阻塞
    if (lock2.acquire(timeout = 2)):
        lock1.release()
        print ('lock2 is locked, lock1 is released')
    else:
        print('acquire lock1 failed')
        lock1.release()

if __name__ == '__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    thread1 = threading.Thread(target = setThread1DeadLock, args = (lock1, lock2))
    thread2 = threading.Thread(target = setThread2DeadLock, args = (lock1, lock2))
    thread1.start()
    thread2.start()