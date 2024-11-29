class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm={0:1}
        psum=0
        res=0
        for num in nums:
            psum=psum+num
            diff=psum-k
            res=res+hm.get(diff,0)
            hm[psum]=1+hm.get(psum,0)
        return res
        



        