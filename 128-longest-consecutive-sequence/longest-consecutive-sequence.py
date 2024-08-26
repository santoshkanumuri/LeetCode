class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if(len(nums)==0):
            return 0

        st=set(nums)
        longest=1
        for num in nums:
            count=1
            if num-1 not in st:
                while(num+1 in st):
                    num=num+1
                    count=count+1
                longest=max(longest,count)
        return longest




        