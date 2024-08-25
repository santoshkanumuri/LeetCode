class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)/2
        pos,neg=[],[]
        for num in nums:
            if(num>0):
                pos.append(num)
            else:
                neg.append(num)
        k,p=0,0
        while(k<n):
            nums[p]=pos[k]
            nums[p+1]=neg[k]
            k+=1
            p+=2
        return nums
        