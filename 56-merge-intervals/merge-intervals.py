class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        for interval in intervals:
            if res==[] or res[-1][1]<interval[0]:
                res.append(interval)
            elif(res[-1][1]<interval[1]):
                res[-1][1]=interval[1]
        return res
