class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        j=-1
        for i in range(n):
            if(nums[i]==0):
                j=i
                break
        if(j==-1):
            return
        for i in range(j+1,n):
            if(nums[i]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        
                

        