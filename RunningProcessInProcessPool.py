# coding=UTF-8
# 判断进程池中正在运行的进程数

import time
from multiprocessing import Pool

def test_sleep(sleep_time):
    time.sleep(sleep_time)
    return 0

if __name__ == '__main__':
    pool = Pool(3)
    pool.apply_async(test_sleep, args = (4, ))
    pool.apply_async(test_sleep, args = (1, ))
    pool.apply_async(test_sleep, args = (5, ))

    while True:
        time.sleep(1)
        processCount = len(pool._cache)
        if processCount != 0:
            print ('{} processes running '.format(processCount))
        else:
            print ('all processes are finished')
            break

    pool.close()
    pool.join()