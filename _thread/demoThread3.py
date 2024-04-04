# demoThread3
import _thread

objLocked = _thread.allocate_lock()

def myFunc(id, msg):
    global objLocked
    while not objLocked.acquire():
        print("{}w/".format(id))
    if (objLocked.locked()):
        objLocked.release()
    print("Thread No.{} ... end game!\n".format(id))
    _thread.exit()

if __name__=="__main__":
    print("get_ident = {}".format(_thread.get_ident()))
    for i in range(2):
        print("run thread No.{}.".format(i))
        _thread.start_new_thread(myFunc, (i, "Ho"))
    print("End of main Program\n")
