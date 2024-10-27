class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={']':'[',')':'(','}':'{'}
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                if stack:
                    if stack[-1]==pairs[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if stack else True
        