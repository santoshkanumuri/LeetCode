class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self, x: int) -> None:
        self.s1.append(x)
        return None
    def pop(self) -> int:
        size=len(self.s1)
        print(self.s1)
        for i in range(size):
            ele=self.s1.pop()
            self.s2.append(ele)
        print(self.s2)
        re=self.s2.pop()
        for i in range(len(self.s2)):
            it=self.s2.pop()
            self.s1.append(it)
        
        return re
        

    def peek(self) -> int:
        if self.s1:
            return self.s1[0]        

    def empty(self) -> bool:
        return len(self.s1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()