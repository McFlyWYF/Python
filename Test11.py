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