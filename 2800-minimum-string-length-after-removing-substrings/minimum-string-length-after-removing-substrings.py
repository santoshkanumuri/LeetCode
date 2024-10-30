class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        c=0
        for char in s:
            if stack and stack[-1]=="A" and char=="B":
                stack.pop()
                c+=1
            elif stack and stack[-1]=="C" and char=="D":
                stack.pop()
                c+=1
            else:
                stack.append(char)
        return len(stack)
            
        