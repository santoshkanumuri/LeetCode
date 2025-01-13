class Solution:
    def minimumLength(self, s: str) -> int:
        c= Counter(s)
        res=0
        for i in list(c.keys()):
            if c[i]>2 and c[i]%2==0:
                res+=2
            elif c[i]>2 and c[i]%2!=0:
                res+=1
            else:
                res+=c[i]
                 
        return res