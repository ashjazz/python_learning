# coding=UTF-8
import queue
import os, time
import threading

def getSthFromQueue(queue):
    queue.join()
    print ('the all_tasks_done lock is release')


def putSthToQueue(queue, name):
    queue.put(name)
    queue.task_done()
    print ('queue has {} task(s)'.format(queue.unfinished_tasks)) #当前队列中剩余的未完成任务数量
    print ('the name is : {}'.format(name))
    time.sleep(5)
    queue.task_done()
    

if __name__ == '__main__':
    name = 'Ash'
    queue = queue.Queue()
    thread1 = threading.Thread(target = getSthFromQueue, args = (queue, ))
    thread2 = threading.Thread(target = putSthToQueue, args = (queue, name, ))
    queue.put(name) #主进程向队列中put一个item，同时unfinished_tasks增加1
    thread1.start()
    time.sleep(2)
    thread2.start()


