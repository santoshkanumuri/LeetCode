class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if(numRows==1):
            return[[1]]
        if(numRows==2):
            return[[1],[1,1]]
        res=[[1],[1,1]]
        for i in range(2,numRows):
            ans=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    ans.append(1)
                else:
                    ans.append(res[i-1][j]+res[i-1][j-1])
            res.append(ans)
        return(res)


        