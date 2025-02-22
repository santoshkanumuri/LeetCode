class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4, 'A':5, 'E':6, 'I':7, 'O':8, 'U':9}
        i = 0
        j = len(s)-1
        sl = list(s)
        while i < j :
            while sl[i] not in arr and i<j:
                i+=1
            while sl[j] not in arr and i<j:
                j-=1
            sl[i], sl[j] = sl[j], sl[i]
            i+=1
            j-=1
        return "".join(sl)
            
        