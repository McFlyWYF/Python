#多进程
#fork()函数调用一次，返回2次,子进程返回0，父进程返回子进程的ID，子进程调用getppid()可以拿到父进程的ID
'''
import os
print ('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print (' I am child process (%s) and my parent is %s' % (os.getpid(),os.getppid()))
else:
    print ('I (%s) just created a child process (%s)' % (os.getpid(),pid))
'''

# multiprocessing 跨平台的多进程模块，提供了一个Process类来代表一个进程对象
from multiprocessing import Process
import os
def run_proc(name):
    print ('Run child process %s (%s)...' % (name,os.getpid()))

if __name__ == '__main__':
    print ('Parent process %s' % os.getpid())
    p = Process(target = run_proc,args = ('test',))
    print ('Child process will start')
    p.start()
    p.join()#等待子进程结束可以继续执行，用于进程间的同步
    print ('Child process end')
print ()
#Pool,启动大量的子进程，使用进程池的方式批量创建子进程
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print ('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print ('Task %s runs %0.2f seconds' % (name,(end - start)))

if __name__ == '__main__':
    print ('Parent process %s ' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args = (i,))
    print ('Waitting for all subprocesses done...')
    p.close()
    p.join()
    print('all subprocesses done')

# 多线程，python提供了2个模块，_thread和threading，大多情况下，只使用threading
import time,threading
def loop():
    print ('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print ('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print ('thread %s ended' % threading.current_thread().name)
print ('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop,name = 'LoopThread')
t.start()
t.join()
print ('thread %s ended' % threading.current_thread().name)
#current_thread()函数，永远返回当前线程的实例。

# lock,多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，多线程中，所有变量都由所有线程共享，任何一个变量都可以被任何一个线程修改。
import time,threading
balance = 0
lock = threading.Lock()#用锁可以使一个变量仅有一个线程来修改，修改完后再继续执行
def change_it(n):
    global balance #共享变量
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()#获取锁
        try:
            change_it(n)
        finally:
            lock.release()#释放锁

t1 = threading.Thread(target = run_thread,args = (5,))
t2 = threading.Thread(target = run_thread,args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print (balance)

import threading,multiprocessing
def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target = loop)
    t.start()