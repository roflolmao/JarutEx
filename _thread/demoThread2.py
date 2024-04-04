# demoThread2
import _thread

def myFunc(id, msg):
    print("ID : {}".format(_thread.get_ident()))
    print("Stack size : {}".format(_thread.stack_size()))
    print("Thread No.{} ... end game!\n".format(id))
    _thread.exit()

if __name__=="__main__":
    print("get_ident = {}".format(_thread.get_ident()))
    for i in range(2):
        print("run thread No.{}.".format(i))
        _thread.start_new_thread(myFunc, (i, "Ho"))
    print("End of main Program\n")
