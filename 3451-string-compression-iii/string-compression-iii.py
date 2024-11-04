class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        while not word=="":
            i=0
            while i<len(word)-1 and i<8 and word[i]==word[i+1]:
                i+=1
            comp=comp+str(i+1)+word[i]
            i+=1
            word=word[i:]
        return comp
    
        

            



        