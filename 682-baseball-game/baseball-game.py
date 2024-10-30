class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for char in operations:
            if char not in ["C","D","+"]:
                stack.append(char)
            if char=="C":
                stack.pop()
            if char=="D":
                stack.append(int(stack[-1])*2)
            if char=="+":
                num1=stack.pop()
                num2=stack.pop()
                stack.append(num2)
                stack.append(num1)
                stack.append(int(num1)+int(num2))
        res=0
        while stack:
            res=res+int(stack.pop())
        return res
        