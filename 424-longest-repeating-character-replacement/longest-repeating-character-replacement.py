class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        maxf=0
        l=0
        hm={}
        for r in range(len(s)):
            hm[s[r]]=1+hm.get(s[r],0)
            maxf=max(maxf,hm[s[r]])
            change=(r-l+1)-maxf
            while (r-l+1-maxf>k):
                hm[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen
            


