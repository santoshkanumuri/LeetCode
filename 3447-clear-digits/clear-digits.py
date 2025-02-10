class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for char in s:
            if char.isnumeric():
                if stack:
                    stack.pop()
                    continue
                else:
                    stack.append(char)
            else:
                if stack and stack[-1].isnumeric():
                    stack.pop()
                    continue
                else:
                    stack.append(char)
        return "".join(stack)

        