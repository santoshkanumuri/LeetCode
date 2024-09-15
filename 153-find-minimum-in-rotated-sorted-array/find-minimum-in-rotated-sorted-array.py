class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(nums[0]<nums[-1]):
            return nums[0]
        if(len(nums)==1):
            return nums[0]
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]<nums[mid-1]):
                return nums[mid]
            if(nums[low]<=nums[mid] and nums[mid]>nums[high]):
                low=mid+1
            else:
                high=mid-1
                if(low==high-1 and nums[low]>nums[high]):
                    return nums[high]
        
        