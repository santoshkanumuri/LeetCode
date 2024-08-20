class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for num in nums:
            # XOR of x with x produce 0 and XOR with 0 produce same element.hence missing number will be the solution
            res=res^num
        return res
        