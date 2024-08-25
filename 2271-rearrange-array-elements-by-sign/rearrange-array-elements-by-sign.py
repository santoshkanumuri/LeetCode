class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res,pos,neg=[0]*n,0,1
        for num in nums:
            if(num>0):
                res[pos]=num
                pos+=2
            else:
                res[neg]=num
                neg+=2
        return res
        
        