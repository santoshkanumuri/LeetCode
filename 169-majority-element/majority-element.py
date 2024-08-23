class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if(count==0):
                target=num
            if(target==num):
                count+=1
            else:
                count-=1
                
        return target
