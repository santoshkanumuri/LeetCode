class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opens=['(','[','{']
        close=[')',']','}']
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                if stack:
                    idx=opens.index(stack[-1])
                    if c==close[idx]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if stack else True
        