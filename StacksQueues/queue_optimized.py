class QueueOptimized:
    def __init__(self): self.s1,self.s2=[],[]
    def enqueue(self,x): self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while self.s1: self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

if __name__=="__main__":
    q=QueueOptimized(); q.enqueue(10); q.enqueue(20)
    print(q.dequeue()) # 10
    q.enqueue(30); print(q.dequeue()) # 20

