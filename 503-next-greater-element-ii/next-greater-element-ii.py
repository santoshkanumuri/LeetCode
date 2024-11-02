class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        nge=nums
        stack=[]
        for i in range(2*n-1):
            while stack and stack[-1][0]<nge[i%n]:
                it=stack.pop()
                res[it[1]%n]=nge[i%n]
            stack.append([nge[i%n],i])
        return res




        


        