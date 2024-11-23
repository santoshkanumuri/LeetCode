class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li=list(s.strip('').split(' '))
        l=len(li)
        print(li,l)
        i=l-1
        while i>0 and li[i]=='':
            i-=1
        return len(li[i])
            
        