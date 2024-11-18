class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        if k==0:
            return [0]*n
        double=code+code
        res=[]
        for i in range(n):
            if k>0:
                arr=double[i+1:i+k+1]
            elif k<0:
                arr=double[i+n-abs(k):i+n]
            res.append(sum(arr))
        
        return res
            
        



        