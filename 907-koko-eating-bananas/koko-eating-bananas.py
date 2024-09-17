class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total=sum(piles)
        if(h==1): return total
        if(len(piles)==0): return 0
        low=1
        high=total
        while(low<=high):
            t=0
            mid=(low+high)//2
            for pile in piles:
                if(pile%mid==0):
                    t+=(pile//mid)
                else:
                    t=t+(pile//mid)+1
            if(t>h):
                low=mid+1
            else:
                high=mid-1
        return low
        
        