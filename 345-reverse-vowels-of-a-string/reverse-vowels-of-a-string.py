class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s)-1
        sl = list(s)
        while i < j and i < len(sl)-1 and j > 0:
            while sl[i] not in arr and i<len(sl)-1 and i<j:
                i+=1
            while sl[j] not in arr and j>0 and i<j:
                j-=1
            sl[i], sl[j] = sl[j], sl[i]
            i+=1
            j-=1
        return "".join(sl)
            
        