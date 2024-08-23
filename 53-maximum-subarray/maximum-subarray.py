class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=nums[0]
        mx=total
        for num in nums[1:]:
            if(total<0):
                total=0
            total=total+num
            mx=max(mx,total)
            
        return mx


