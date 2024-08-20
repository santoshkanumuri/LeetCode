class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n:int=len(nums)
        res:int=(n*(n+1))/2
        for item in nums:
            res=res-item
        return int(res)
        