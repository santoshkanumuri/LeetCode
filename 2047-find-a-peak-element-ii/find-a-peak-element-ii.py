class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m:int=len(mat)
        n:int=len(mat[0])
        low:int=0
        high:int=n-1
        while(low<=high):
            l:int=-1
            r:int=-1
            mid=(low+high)//2
            mx,mx_ind=mat[0][mid],0
            for i in range(m):
                if(mx<mat[i][mid]):
                    mx_ind=i
                    mx=mat[i][mid]
            print(mx_ind,mid)
            if(mid!=0):
                l=mat[mx_ind][mid-1]
            if(mid<n-1):
                r=mat[mx_ind][mid+1]
            if(mat[mx_ind][mid]>l and mat[mx_ind][mid]>r):
                print(mat[mx_ind][mid],l,r)
                return [mx_ind,mid]
            elif(mat[mx_ind][mid]<=l):
                high=mid-1
            else:
                low=mid+1
            

            
