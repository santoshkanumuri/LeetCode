class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mx:int=max(weights)
        low:int = mx
        high:int = sum(weights)
        n:int=len(weights)
        last:int=0
        while(low<=high):
            dcount:int=0
            cap:int=0
            mid:int=(low+high)//2
            for i in range(n):
                if((cap+weights[i])<=mid):
                    cap=cap+weights[i]
                if(i!=n-1 and cap+weights[i+1]>mid):
                    dcount+=1
                    cap=0
                elif(i==n-1):
                    dcount+=1
            if(dcount<=days):
                last=mid
                high=mid-1
            else:
                low=mid+1
        return last



        