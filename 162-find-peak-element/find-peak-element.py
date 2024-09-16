class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        low=1
        high=n-2
        if(n==1): return 0
        if(nums[0]>nums[1]): return 0
        if(nums[-1]>nums[-2]): return n-1
        while(low<=high):
            print(low,high)
            mid=(low+high)//2
            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            elif(nums[mid-1]<nums[mid] and nums[mid]<nums[mid+1]):
                low=mid+1
            else:
                high=mid-1
        return mid
        