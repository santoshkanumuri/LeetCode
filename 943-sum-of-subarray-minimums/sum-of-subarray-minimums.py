class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def nse(nums):
            n=len(nums)
            res=[n]*n
            stack=[]
            for idx,num in enumerate(nums):
                while stack and stack[-1][0]>num:
                    it=stack.pop()
                    res[it[1]]=idx
                stack.append([num,idx])
            return res

        def pse(nums):
            n=len(nums)
            res=[-1]*n
            stack=[]
            for idx,num in enumerate(nums[::-1]):
                idx=n-idx-1
                while stack and stack[-1][0]>=num:
                    it=stack.pop()
                    res[it[1]]=idx
                stack.append([num,idx])
            return res
        p=pse(arr)
        n=nse(arr)
        total=0
        mod=1000000007
        for i in range(len(arr)):
            left=i-p[i]
            right=n[i]-i
            total=total+((left*right*arr[i])%mod)
            total=total%mod
        return total

        



        