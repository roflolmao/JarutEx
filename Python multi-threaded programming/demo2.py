# -*- coding: UTF-8 -*-
import threading
import time
class myThread(threading.Thread):
	def __init__( self, thread_id, name, counter ):
		threading.Thread.__init__( self )
		self.thread_id = thread_id
		self.name = name
		self.counter = counter
	def run( self ):
		print("Starting "+self.name)
		print_time( self.name, self.counter, 5 )
		print("Exit "+self.name)
running = 0
def print_time( thread_name, delay, counter ):
	while counter:
		if running:
			thread_name.exit()
		time.sleep(delay)
		print(thread_name +":"+str(time.ctime(time.time())))
		counter -= 1
def main():
	thread1 = myThread(1, "thread-1", 1)
	thread2 = myThread(2, "thread-2", 2)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	print("Exiting Main Thread")

if __name__=="__main__":
	main()
