class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findrow(mat: List[List[int]], k: int, m: int):
            low:int=0
            high:int=m-1
            while(low<=high):
                print(low,high)
                mid:int=(low+high)//2
                if(mat[mid][0]<=k and mat[mid][-1]>=k):
                    return mid
                elif(mat[mid][0]>k):
                    high=mid-1
                else:
                    low=mid+1
            return -1


        m=len(matrix)
        n=len(matrix[0])
        row=findrow(matrix,target,m)
        if(row==-1):
            return False
        low:int=0
        high:int=n-1
        while(low<=high):
            mid:int=(low+high)//2
            if(matrix[row][mid]==target):
                return True
            elif(matrix[row][mid]>target):
                high=mid-1
            else:
                low=mid+1
        return False

        