class Solution:
    def helper(self,it1,it2,token):
        it1=int(it1)
        it2=int(it2)
        if token=='*':
            return it1*it2
        if token=="+":
            return it1+it2
        if token=='-':
            return it1-it2
        if token=='/':
            return it1/it2
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token in ['*','+','-','/']:
                it2=stack.pop()
                it1=stack.pop()
                res=self.helper(it1,it2,token)
                stack.append(res)
            else:
                stack.append(token)
        return int(stack.pop())


        