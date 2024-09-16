class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=len(nums)
        low=1
        high=l-2
        if(l==1):return nums[0]
        if(nums[0]!=nums[1]):return nums[0]
        if(nums[l-1]!=nums[l-2]):return nums[l-1]
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
                return nums[mid]
            if(mid%2==0 and nums[mid]==nums[mid-1]):
                high=mid-1
            elif(mid%2==1 and nums[mid]==nums[mid+1]):
                high=mid-1
            else:
                low=mid+1

        return nums[mid]

            
        