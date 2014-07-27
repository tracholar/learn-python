# coding:gbk

import os
from multiprocessing import Process


def print_time(pname, delay):
	while True:
		time.sleep(delay)
		print '[%d] %s : %s' % (os.getppid(), tname,time.ctime(time.time()))


p1 = Process(target=print_time,args=('P1',2))
p2 = Process(target=print_time,args=('P2',3))

p1.start()
p2.start()

p1.join()
p2.join()