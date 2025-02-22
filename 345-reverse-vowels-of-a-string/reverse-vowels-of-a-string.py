class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = ['a','e','i','o','u','A','E','I','O','U']
        stack = []
        for char in s:
            if char in arr:
                stack.append(char)
        
        for i in range(len(s)):
            if s[i] in arr:
                if stack:
                    ele = stack.pop()
                    s = s[:i] + ele + s[i+1:]
        
        return s

        