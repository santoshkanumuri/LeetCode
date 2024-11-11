class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        l=0
        r=n-1
        while l!=r and l<n-1 and r>0:
            print(s[l],s[r])
            if not s[l].isalnum():
                print(s[l])
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower()!=s[r].lower():
                print(s[l],s[r])
                return False
            l+=1
            r-=1
        return True
        