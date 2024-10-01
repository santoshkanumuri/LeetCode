class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s:int=0
        f:int=0
        s2:int=0
        while True:
            s=nums[s]
            f=nums[nums[f]]
            if(s==f):
                break
        
        while True:
            s2=nums[s2]
            s=nums[s]
            if(s2==s):
                return s2

        