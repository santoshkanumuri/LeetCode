class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map={}
        for num in nums:
            if map.get(num,0)==0:
                map[num]=1
            else:
                map[num]+=1
        itr=0
        for item in map.keys():
            nums[itr]=item
            itr+=1
        return(len(list(map.keys())))
        
        