class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        l=0
        hm={}
        res=0
        for r in range(n):
            hm[s[r]]=r
            l=min(hm.get('a',-1),hm.get('b',-1),hm.get('c',-1))
            if l>=0:
                res=res+l+1
            
        return res




        