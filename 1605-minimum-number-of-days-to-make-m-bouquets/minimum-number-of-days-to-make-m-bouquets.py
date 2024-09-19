class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ndays=len(bloomDay)
        if(ndays<m*k):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        lmid=-1
        blen=0
        while(low<=high):
            bcount=0
            blen=0
            mid=(low+high)//2
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
            if(bcount<m):
                low=mid+1
        return lmid


        