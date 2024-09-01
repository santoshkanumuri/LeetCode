class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n:int=len(nums)
        nums.sort()
        res:List[int]=[]
        total:int=0
        for i in range(n):
            if(i!=0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=n-1
            while(j<k):
                total=nums[i]+nums[j]+nums[k]
                if(total<0):
                    j+=1
                elif(total>0):
                    k-=1
                else:
                    li=[nums[i],nums[j],nums[k]]
                    res.append(li)
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
        return res


                
        