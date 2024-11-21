class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_idx = 0
        min_len=10000000
        res=""
        for i in range(len(strs)):
            st=strs[i]
            l=len(st)
            
            if l<min_len:
                min_len=l
                min_idx=i
        print(strs[min_idx])
        
        for i in range(min_len):
            for st in strs:
                if st[i]!=strs[min_idx][i]:
                    return res
            res=res+strs[min_idx][i]
        return res
