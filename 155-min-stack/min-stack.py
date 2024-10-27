class MinStack:

    def __init__(self):
        self.stack=[]
        self.mins=[]

    def push(self, val: int) -> None:
        m=min(val,self.mins[-1]) if self.mins else val
        self.mins.append(m)
        self.stack.append(val)
        return None
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        return None
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()