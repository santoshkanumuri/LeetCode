class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                si,st=stack.pop()
                res[si]=i-si
            stack.append([i,t])
        return res



            
