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

#ThreadLocal,定义一个全局变量，然后绑定自己的局部变量，让每个线程访问自己的变量
import threading
#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print ('Hello, %s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread,args = ('Alice',),name = 'Thread-A')
t2 = threading.Thread(target = process_thread,args = ('Bob',),name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

#进程 VS 线程
'''Master-Worker模式，Master负责分配任务,Worker负责执行任务，在多任务环境下，通常是一个Master,多个Worker.
多进程实现Master-Worker,主进程是Master,其他进程是Worker
多线程实现Master-Worker，主线程是Master,其他线程是Worker

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。多进程模式的缺点是创建进程的代价大.

多线程模式通常比多进程快一点,多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。'''

#线程切换
#计算密集型 VS IO密集型
'''计算密集型任务的特点是要进行大量的计算，消耗CPU资源.'''
#异步IO

#分布式进程
#，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
# managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
#服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务。
import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#从BaseManager继承的Queuemanager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')

#在另一台机器上启动任务进程（本机上启动也可以）：
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')