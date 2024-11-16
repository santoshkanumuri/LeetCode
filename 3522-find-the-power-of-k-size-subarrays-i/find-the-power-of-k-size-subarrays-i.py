class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def sub(l,r):
            print(nums[l:r])
            for i in range(l+1,r):
                if (nums[i-1]!=nums[i]-1):
                    return -1
            return nums[r-1]

        l=0
        res=[]
        for r in range(l+k,len(nums)+1):
            res.append(sub(l,r))
            l+=1
        return res


                



        