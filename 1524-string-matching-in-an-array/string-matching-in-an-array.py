class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words=list(set(words))
        res=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if words[i] in words[j]:
                        res.append(words[i])
                        break
        return res
            
        