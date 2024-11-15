class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1): return False
        hm1,hm2=[0]*26,[0]*26
        s1len,s2len=len(s1),len(s2)


        for i in range(s1len):
            hm1[ord(s1[i])-97]+=1
            hm2[ord(s2[i])-97]+=1
        l=0
        if hm1==hm2:
            return True
        for r in range(s1len,s2len):
            if(hm1!=hm2):
                hm2[ord(s2[l])-97]-=1
                hm2[ord(s2[r])-97]+=1
                l+=1
            if hm1==hm2:
                return True
            
        return False


            


        