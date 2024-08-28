class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        for i in range(rows):
            for j in range(i,rows):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            matrix[i]=matrix[i][::-1]
