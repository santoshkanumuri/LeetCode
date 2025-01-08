class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(s1, s2):
            if len(s2)<len(s1):
                return False
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    return False
            s1=s1[::-1]
            s2=s2[::-1]
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    return False
            return True
        res=0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if i<j:
                    if isPrefixAndSuffix(words[i], words[j]):
                        print(i,j)
                        res+=1
        return res



        