class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        columns=len(matrix[0])
        col0=1
        '''this solution o(1) extra space and 2(n*m) time complexity'''

        '''use first row as the column marker and first column as row marker'''

        for i in range(rows):
            for j in range(columns):
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    if(j!=0):
                        matrix[0][j]=0
                    else:
                        col0=0
        '''start modifying matrix from second row and second column '''
        for i in range(1,rows):
            for j in range(1,columns):
                if(matrix[i][0]==0 or matrix [0][j]==0):
                    matrix[i][j]=0

        ''' mosify first row from last since it is dependent on first column'''
        if(matrix[0][0]==0):
            for j in range(1,columns):
                matrix[0][j]=0

        '''finally modify first column'''
        if(col0==0):
            for i in range(rows):
                matrix[i][0]=0
        



                    
        