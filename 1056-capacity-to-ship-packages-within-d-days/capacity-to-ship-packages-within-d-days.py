class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low:int = 0
        high:int = sum(weights)
        n:int=len(weights)
        mx:int=max(weights)
        last:int=0
        while(low<=high):
            dcount:int=0
            cap:int=0
            mid:int=(low+high)//2
            if(mx>mid):
                low=mid+1
                continue
            for i in range(n):
                weight:int=weights[i]
                if((cap+weight)<=mid):
                    cap=cap+weight
                if(i!=n-1 and cap<=mid and cap+weights[i+1]>mid):
                    dcount+=1
                    cap=0
                elif(i==n-1 and cap<=mid and cap!=0):
                    dcount+=1
            print(dcount,mid)
            if(dcount<=days):
                last=mid
                high=mid-1
            else:
                low=mid+1
        return last



        