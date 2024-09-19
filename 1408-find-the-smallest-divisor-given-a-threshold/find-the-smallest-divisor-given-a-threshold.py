class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low:int=1
        high:int=max(nums)
        while(low<=high):
            total:int=0
            mid:int=(low+high)//2
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

        