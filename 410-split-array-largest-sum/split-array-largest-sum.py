class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def possible(mid,nums,n):
            c=0
            total=0
            for i in range(n):
                if(total+nums[i]<=mid):
                    total+=nums[i]
                else:
                    c+=1
                    total=nums[i]
            return c


        n=len(nums)
        low=max(nums)
        high=sum(nums)

        while(low<=high):
            mid=(low+high)//2
            parts=possible(mid,nums,n)
            if(parts>=k):
                low=mid+1
            else:
                high=mid-1
        return low


        