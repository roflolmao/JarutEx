# demoThread1
import _thread
# demoThread1
import _thread
import time
import random

runningTimes = [random.randint(3,8), random.randint(2,5)]

def myFunc(delay, id):
    global runningTimes  
    while (runningTimes[id] > 0):
        time.sleep(delay)
        print('Running thread No.{} with delay = {}.'.format(id, delay))
        runningTimes[id] -= 1
    print("Thread No.{} ... end game!".format(id))
    _thread.exit()

if __name__=="__main__":
    for i in range(2):
        print("run thread No.{}, {} times.".format(i, runningTimes[i]))
        _thread.start_new_thread(myFunc, (random.randint(1, 4), i))
    print("End of main Program")
