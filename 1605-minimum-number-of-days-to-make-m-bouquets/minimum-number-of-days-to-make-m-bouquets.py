class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ndays:int=len(bloomDay)
        if(ndays<m*k):
            return -1
        low:int=min(bloomDay)
        high:int=max(bloomDay)
        lmid:int =-1
        while(low<=high):
            bcount:int=0
            blen:int=0
            mid:int=(low+high)//2
            for i in range(ndays):
                if(bloomDay[i]<=mid):
                    blen=blen+1
                    if(blen==k):
                        bcount+=1
                        blen=0
                else:
                    blen=0
            if(bcount>=m):
                lmid=mid
            if(bcount>=m and m*k>=mid):
                return mid
            elif(bcount>=m and m*k<mid):
                high=mid-1
            elif(bcount<m):
                low=mid+1
        return lmid


        