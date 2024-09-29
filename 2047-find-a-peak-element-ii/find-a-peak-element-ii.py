class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def find(mat,i,j):
            l:int=-1
            r:int=-1
            u:int=-1
            d:int=-1
            c:int=0
            m:int=len(mat)
            n:int=len(mat[0])
            print(i,j)
            

            if(not i==0):
                u=mat[i-1][j]
            if(not j==0):
                l=mat[i][j-1]
            if(i!=m-1):
                d=mat[i+1][j]
            if(j!=n-1):
                r=mat[i][j+1]
            print(l,r,u,d)
            for ele in [l,r,u,d]:
                if(mat[i][j]>ele):
                    c+=1

            return c==4

        

        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                if(find(mat,i,j)):
                    return [i,j]



        