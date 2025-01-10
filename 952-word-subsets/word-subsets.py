class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hm=defaultdict(int)
        for word in words2:
            wmap=Counter(word)
            for i,j in wmap.items():
                hm[i] = max(hm[i],j)
        
        
        def check(hm2):
            count=0
            for i in hm.keys():
                if hm2[i]>=hm[i]:
                    count+=1
            return count==len(hm.keys())
        res=[]
        for word in words1:
            c=Counter(word)
            if check(c):
                res.append(word)
        
        return res
            


        