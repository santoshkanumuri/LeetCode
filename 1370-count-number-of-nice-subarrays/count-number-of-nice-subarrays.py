class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def isOdd(num):
            return num%2 != 0
        def find(k):
            l=0
            count=0
            res=0
            r=0
            while r<len(nums):
                if isOdd(nums[r]):
                    count+=1
                while count>k:
                    if isOdd(nums[l]):
                        count-=1
                    l+=1
                r+=1
                res=res+(r-l+1)
            return res 
        
        ans=find(k)-find(k-1)
        return ans





        