class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        maxlen=0
        r=0
        z=0
        while r<len(nums):
            if nums[r]==0:
                z+=1
            if z<=k:
                maxlen=max(maxlen,r-l+1)
            while z>k and l<r:
                if nums[l]==0:
                    z-=1
                l+=1
            r+=1
        return maxlen

        