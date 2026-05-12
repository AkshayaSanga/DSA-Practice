class QueueNaive:
    def __init__(self): self.s1,self.s2=[],[]
    def enqueue(self,x): self.s1.append(x)
    def dequeue(self):
        while self.s1: self.s2.append(self.s1.pop())
        val=self.s2.pop() if self.s2 else None
        while self.s2: self.s1.append(self.s2.pop())
        return val

if __name__=="__main__":
    q=QueueNaive(); q.enqueue(1); q.enqueue(2)
    print(q.dequeue()) # 1
    q.enqueue(3); print(q.dequeue()) # 2

