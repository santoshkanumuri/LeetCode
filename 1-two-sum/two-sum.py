class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        n=len(nums)
        for i in range(n):
            if(hash_map.get(target-nums[i],-1)==-1):
                hash_map[nums[i]]=i
            else:
                return [hash_map[target-nums[i]],i]
       
        



        
