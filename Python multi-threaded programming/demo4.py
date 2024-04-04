# -*- coding: UTF-8 -*-
import threading
import time
import queue

running = 1
thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["One", "Two", "Three", "Four", "Five"]
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
thread_ID = 1

def process_data(thread_name, q):
	while running:
		queue_lock.acquire()
		if not work_queue.empty():
			data = q.get()
			queue_lock.release()
			print( thread_name+" processing "+data)
		else:
			queue_lock.release()
			time.sleep(1)
class myThread(threading.Thread):
	def __init__( self, thread_id, name, q ):
		threading.Thread.__init__( self )
		self.thread_id = thread_id
		self.name = name
		self.q = q
	def run( self ):
		print("Starting "+self.name)
		process_data(self.name, self.q)
		print("Exit "+self.name)

for t_name in thread_list:
	thread = myThread(thread_ID, t_name, work_queue)
	thread.start()
	threads.append(thread)
	thread_ID += 1
queue_lock.acquire()
for word in name_list:
	work_queue.put(word)
queue_lock.release()
while not work_queue.empty():
	pass
running = False
for t in threads:
	t.join()
print ("Exiting Main Thread")
thread_lock = threading.Lock()
threads = []
