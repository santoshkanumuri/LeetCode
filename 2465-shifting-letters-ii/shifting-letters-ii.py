class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        p= [0]* (len(s)+1)
        s= [ord(c) - ord('a') for c in s]
        for arr in shifts:
            start,end,d=arr
            p[end+1]+=1 if d else -1 
            p[start]+=-1 if d else 1
        
        diff=0
         
        for i in reversed(range(len(p))):
            diff+=p[i]

            s[i-1]=(s[i-1]+diff)%26
        
        
        s=[chr(i + ord('a')) for i in s]
        return "".join(s)        