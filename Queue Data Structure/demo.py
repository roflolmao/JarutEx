class Queue:
    def __init__(self,maxN=10):
        self.items = []
        self.idx = 0
        self.topOfQ = maxN
    def push(self,x):
        if self.idx == self.topOfQ:
            print("Queue Overflow!")
            return
        self.items.append(x)
        self.idx += 1
    def pop(self):
        return 0
myQueue = Queue(5)

for i in range(7):
    myQueue.push(i)
    print(myQueue.items)
