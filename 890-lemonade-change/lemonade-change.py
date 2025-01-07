class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hm={5:0,10:0,20:0}

        for bill in bills:
            if bill==20:
                if (hm[5]>=1 and hm[10]>=1):
                    hm[5]-=1
                    hm[10]-=1
                    hm[20]+=1
                elif(hm[5]>=3):
                    hm[5]-=3
                    hm[20]+=1
                else:
                    return False
            elif bill==10:
                if hm[5]>=1:
                    hm[5]-=1
                    hm[10]+=1
                else:
                    return False
            elif bill==5:
                hm[5]+=1
            
        return True
            
                
        