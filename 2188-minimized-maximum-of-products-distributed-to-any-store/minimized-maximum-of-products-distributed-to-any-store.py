class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        total=sum(quantities)
        if n==1:
            return total
        if n>total:
            return 1
        def distribute(pro):
            shops=0
            quan=quantities
            for q in quan:
                while q>=pro:
                    shops+=1
                    q=q-pro
                if q<pro and q!=0:
                    shops+=1
                    q=0
            return shops

        l=0
        h=total
        res=total
        while l<=h:
            mid=(l+h)//2
            s=distribute(mid)
            if s>n:
                l=mid+1
            elif s<=n:
                res=min(res,mid)
                h=mid-1
        return res
            



        