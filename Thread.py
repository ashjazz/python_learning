# coding=UTF-8
# 线程的基础方法
import threading
import datetime
import os, time

def thread_run(num):
    time.sleep(num)
    now = datetime.datetime.now()
    # 打印当前线程的名称
    print ('线程名： {}, now is {}'.format(threading.currentThread().getName(), now))

def main(thread_num):
    thread_list = list()
    for i in range(thread_num):
        thread_name = 'thread_{}'.format(i)
        # 创建线程并将其添加至线程列表中
        thread_list.append(threading.Thread(target = thread_run, name = thread_name, args = (2, )))

    for each_thread in thread_list:
        each_thread.setName('goods')
        # 判断线程是否活着
        print (each_thread.is_alive())
        # 返回线程的ID
        print (each_thread.ident)
        each_thread.start()
        print (each_thread.ident)
        print (each_thread.is_alive())
        each_thread.join()
        print (each_thread.is_alive())

if __name__ == '__main__':
    main(3)