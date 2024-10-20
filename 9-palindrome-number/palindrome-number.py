class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x%10==0 and x) or x<0:
            return False
        
        newnum=0
        c=x
        while x:
            rem=x%10
            newnum=newnum*10+rem
            x=x//10
        return c==newnum

        