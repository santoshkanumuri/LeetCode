class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        low=1
        high=max(nums)
        mindivisor=0
        while(low<=high):
            total=0
            mid=(low+high)//2
            for num in nums:
                if(num%mid==0):
                    total+=num//mid
                else:
                    total+=(num//mid)+1
            if(total<=threshold):
                print(low,mid,high,total)
                mindivisor=mid
                high=mid-1
            else:
                print(mid,total)
                low=mid+1
        return mindivisor

        