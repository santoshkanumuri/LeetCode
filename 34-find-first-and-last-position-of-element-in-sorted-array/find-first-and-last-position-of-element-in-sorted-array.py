class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                l,h=mid,mid
                while(l>0 and nums[l-1]==target):
                    l-=1
                while(h<len(nums)-1 and nums[h+1]==target):
                    h+=1
                return [l,h]
            elif(nums[mid]>target):
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]
        