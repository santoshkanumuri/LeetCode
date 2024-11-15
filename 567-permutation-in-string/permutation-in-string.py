class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        hm1=[0]*26
        for char in s1:
            hm1[ord(char)-97]+=1
        l=0
        r=len(s1)
        hm2=[0]*26
        for i in range(l,r):
            char=s2[i]
            hm2[ord(char)-97]+=1
        if hm1==hm2:
            return True
        
        while r<len(s2):
            if hm1==hm2:
                return True
            else:
                print(hm1,hm2)
                hm2[ord(s2[l])-97]-=1
                hm2[ord(s2[r])-97]+=1
                l+=1
                r+=1
                print(hm1,hm2)
            if hm1==hm2:
                return True
            
        return False


            


        