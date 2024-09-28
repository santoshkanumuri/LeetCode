class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: int=len(matrix)
        n: int=len(matrix[0])
        row: int=m-1
        col: int=0
        while(row>=0 and col<n):
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]>target):
                row-=1
            else:
                col+=1
        return False

        