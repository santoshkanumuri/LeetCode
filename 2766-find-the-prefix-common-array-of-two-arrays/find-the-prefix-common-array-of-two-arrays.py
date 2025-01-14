class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c1=defaultdict(int)
        c2=defaultdict(int)
        res=[]
        for i in range(len(A)):
            count=0
            c1[A[i]]+=1
            c2[B[i]]+=1
            for key in list(c1.keys()):
                if c1[key]==c2[key]:
                    count+=1
            res.append(count)
        return res
