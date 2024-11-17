class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1 or k==1:
            return nums
        l=0
        res=[] 
        count=1
        for r in range(len(nums)):
            if r>0 and nums[r-1]==nums[r]-1:
                count+=1
            if r-l+1>k:
                count-=1 if nums[l]==nums[l+1]-1 else 0
                l+=1
            if r-l+1==k:
                res.append(nums[r] if count==k else -1)
            
        return res


                



        