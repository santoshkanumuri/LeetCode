class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        maxf=0
        l=0
        hm=[0]*26
        n=len(s)
        for r in range(n):
            hm[ord(s[r])-65]+=1
            maxf=max(maxf,hm[ord(s[r])-65])
            change=(r-l+1)-maxf
            if change<=k:
                maxlen=max(maxlen,r-l+1)
            else:
                while (r-l+1-maxf>k):
                    hm[ord(s[l])-65]-=1
                    l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen
            


