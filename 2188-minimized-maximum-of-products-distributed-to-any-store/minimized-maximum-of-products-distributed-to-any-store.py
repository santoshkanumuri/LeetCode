class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        total=sum(quantities)
        if n==1:
            return total
        if n>total:
            return 1
        def can_distribute(pro):
            shops=0
            for q in quantities:
                shops += math.ceil(q/pro)
            print(shops,pro)
            return shops<=n

        l=0
        h=max(quantities)
        res=0
        while l<=h:
            mid=(l+h)//2
            if can_distribute(mid):
                res=mid
                h=mid-1
            else:
                l=mid+1
        return res
            



        