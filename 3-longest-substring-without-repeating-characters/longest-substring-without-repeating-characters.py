class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        res=set()
        hm={}
        l=0
        mx=0
        for r in range(len(s)):
            if s[r] in hm:
                l=max(hm[s[r]]+1,l)
                hm[s[r]]=r
            else:
                hm[s[r]]=r
            mx=max(mx,r-l+1)
        return mx

