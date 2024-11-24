class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def find(k):
            if k<0:
                return 0
            l:int=0
            count:int=0
            res:int=0
            for r in range(len(nums)):
                if nums[r]%2==1:
                    count+=1
                while count>k:
                    if nums[l]%2==1:
                        count-=1
                    l+=1
                res=res+(r-l+1)
            return res 
        
        ans=find(k)-find(k-1)
        return ans





        