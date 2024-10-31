class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        for idx,num in enumerate(nums):
            while stack and stack[-1][0]<num:
                it=stack.pop()
                res[it[1]]=num
            stack.append([num,idx])
        for idx,num in enumerate(nums):
            while stack and stack[-1][0]<num:
                it=stack.pop()
                res[it[1]]=num
            stack.append([num,idx])
        
        return res


        