class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        res=[]
        for idx,interval in enumerate(intervals,start=0):
            if idx==0 or res[-1][1]<interval[0]:
                res.append(interval)
            elif(res[-1][1]<interval[1]):
                res[-1][1]=interval[1]
        return res
