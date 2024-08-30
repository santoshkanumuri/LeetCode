class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        co=Counter(nums)
        res=[]
        n=len(nums)
        for key,value in co.items():
            if(value>n//3):
                res.append(key)
        return res

        