# coding:gbk

import thread
import time

def print_time(tname, delay):
	while True:
		time.sleep(delay)
		print '%s : %s' % (tname,time.ctime(time.time()))
		
thread.start_new_thread(print_time,('T1', 2))
thread.start_new_thread(print_time,('T2', 3))

while True:
	pass