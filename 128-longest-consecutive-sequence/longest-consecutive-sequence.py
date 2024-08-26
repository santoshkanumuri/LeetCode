class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums==[]):
            return 0
        hashmap={}
        count,longest=1,1
        for num in nums:
            if(hashmap.get(num,0)==0):
                hashmap[num]=1
            else:
                hashmap[num]+=1
        for num in nums:
            if(hashmap.get(num-1,0)==0):
                while(hashmap.get(num+1,0)>0):
                    count+=1
                    num+=1
                longest=max(longest,count)
                count=1
        return longest


        