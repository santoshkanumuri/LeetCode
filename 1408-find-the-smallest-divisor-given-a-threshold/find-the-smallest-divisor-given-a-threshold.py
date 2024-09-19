class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while(low<=high):
            total=0
            mid=(low+high)//2
            for num in nums:
                if(num%mid==0):
                    total+=num//mid
                else:
                    total+=(num//mid)+1
            if(total<=threshold):
                high=mid-1
            else:
                low=mid+1

        return low

        