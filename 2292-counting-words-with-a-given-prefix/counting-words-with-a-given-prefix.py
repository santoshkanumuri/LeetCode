class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        def isSuffix(word):
            for i in reversed(range(len(pref))):
                    if word[i]!=pref[i]:
                        return False
            return True

        res=0
        for word in words:
            if len(word)>=len(pref):  
                if isSuffix(word):
                    res+=1
        return res
                    

        