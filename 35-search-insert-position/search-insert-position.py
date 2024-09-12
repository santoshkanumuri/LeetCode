class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums==[]):
            return 0
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                high=mid-1
            else:
                low=mid+1
        if(target<nums[mid]):
            return mid
        else:
            return mid+1
        