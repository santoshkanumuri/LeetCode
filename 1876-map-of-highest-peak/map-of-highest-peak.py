class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q=collections.deque()
        m=len(isWater)
        n=len(isWater[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        visit=set()


        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    res[i][j]=0
                    q.append((i,j))
                    visit.add((i,j))
        
        while q:
            
            row,col=q.popleft()
            if row>0 and (row-1,col) not in visit:
                
                res[row-1][col]=res[row][col]+1 
                q.append((row-1,col))
                visit.add((row-1,col))
            if col>0 and (row,col-1) not in visit:
                
                res[row][col-1]=res[row][col]+1 
                q.append((row,col-1))
                visit.add((row,col-1))
            if col+1<n and (row,col+1) not in visit:
                
                res[row][col+1]=res[row][col]+1 
                q.append((row,col+1))
                visit.add((row,col+1))
            if row+1<m and (row+1,col) not in visit:
                
                res[row+1][col]=res[row][col]+1 
                q.append((row+1,col))
                visit.add((row+1,col))
        
        return res
            



