class StackArray:
    def __init__(self, capacity=5):
        self.arr = [None]*capacity; self.top=-1; self.capacity=capacity
    def push(self, x):
        if self.top==self.capacity-1: return "Overflow"
        self.top+=1; self.arr[self.top]=x
    def pop(self):
        if self.top==-1: return "Underflow"
        val=self.arr[self.top]; self.top-=1; return val
    def peek(self): return self.arr[self.top] if self.top!=-1 else None
    def is_empty(self): return self.top==-1

if __name__ == "__main__":
    s=StackArray(); s.push(5); s.push(15)
    print(s.peek())   # 15
    print(s.pop())    # 15
    print(s.is_empty()) # False

