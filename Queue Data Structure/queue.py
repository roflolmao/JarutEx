class Queue:
    def __init__(self,maxN=10):
        self.items = []
        self.idx = 0
        self.topOfQ = maxN
    def push(self,x):
        if self.idx == self.topOfQ:
            print("Queue Overflow!")
            return False
        self.items.append(x)
        self.idx += 1
        return True
    def pop(self):
        if self.idx == 0:
            print("Queue empty!")
            return None
        self.idx -= 1
        self.items.reverse()
        x = self.items.pop()
        self.items.reverse()
        return x
