class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        hm={}
        for r in range(len(nums)):
            if hm.get(nums[r],-1) == -1:
                hm[nums[r]]=r
            elif abs(hm[nums[r]]-r)<=k:
                return True
            else:
                hm[nums[r]]=r
    
        return False
                


        