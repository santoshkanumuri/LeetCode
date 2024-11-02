class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        nge=nums+nums
        stack=[]
        for i in range(len(nge)):
            while stack and stack[-1][0]<nge[i]:
                it=stack.pop()
                res[it[1]%n]=nge[i]
            stack.append([nge[i],i])
        return res




        


        