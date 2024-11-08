class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for char in s:
            if stack1 and char=="#":
                stack1.pop()
            elif not stack1 and char=="#":
                pass
            else:
                stack1.append(char)
        for char in t:
            if stack2 and char=="#":
                stack2.pop()
            elif not stack2 and char=="#":
                pass
            else:
                stack2.append(char)
        print(stack1,stack2)
        return stack1==stack2

        