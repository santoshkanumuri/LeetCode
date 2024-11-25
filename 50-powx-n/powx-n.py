class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if x==0: return 0
        def absolute(x,n):
            if n==1:
                return x
            else:
                l=absolute(x*x,n//2)
                return x*l if n%2 else l



        res=absolute(x,abs(n))
        return res if n>0 else 1/res
        
        