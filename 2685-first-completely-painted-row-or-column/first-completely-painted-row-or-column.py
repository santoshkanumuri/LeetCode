class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hm={}
        m=len(mat)
        n=len(mat[0])

        for i in range(m):
            for j in range(n):
                hm[mat[i][j]]=(i,j)
        row=[0]*m
        col=[0]*n
       
        for i in range(len(arr)):
            num=arr[i]
            r,c=hm.get(num)
            row[r]+=1
            col[c]+=1
           
            if row[r]==n or col[c]==m:
                return i
