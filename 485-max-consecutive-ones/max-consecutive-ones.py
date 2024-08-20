class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        max_c=0
        count=0
        j=-1
        for i in range(n):
            if(nums[i]==1):
                j=i
                break
        if(j==-1): return 0
        for i in range(j,n):
            if(nums[i]==1):
                count+=1
            else:
                count=0
            if(max_c<count):
                max_c=count
        return max_c

        