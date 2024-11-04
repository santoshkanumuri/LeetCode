class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        i=0
        while not word=="":
            i=0
            count=1
            while i<len(word)-1 and count<9 and word[i]==word[i+1]:
                i+=1
                count+=1
            comp=comp+str(count)+word[i]
            i+=1
            word=word[i:]
        return comp
    
        

            



        