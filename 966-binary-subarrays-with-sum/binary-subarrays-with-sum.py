class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count(k):
            if k<0:
                return 0
            l=0
            r=0
            total=0
            count=0
            while r<len(nums):
                total=total+nums[r]
                while total>k:
                    total=total-nums[l]
                    l+=1
                count=count+r-l+1
                r+=1
            return count
        
        plus=count(goal)
        res=plus-count(goal-1)
        return res

