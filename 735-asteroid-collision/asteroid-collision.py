class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        res=[]
        for ast in asteroids:
            if(ast<0):
                pair=[0-ast,"m"]
            else:
                pair=[ast,"p"]
            stack.append(pair)
            for i in range(len(stack)-1,0,-1):
                if len(stack)>i:
                    if stack[i][1]=="m" and stack[i-1][1]=="p":
                        if stack[i][0]>stack[i-1][0]:
                            stack.pop(i-1)
                        elif stack[i][0]<stack[i-1][0]:
                            stack.pop(i)      
                        else:
                            stack.pop(i)
                            stack.pop(i-1)          
        for it in stack:
            if it[1]=="m":
                res.append(0-it[0])
            else:
                res.append(it[0])
        return res
            
            



        