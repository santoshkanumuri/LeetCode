class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hash_arr=[0]*3
        for num in nums:
            hash_arr[num]+=1
        count=0
        for i in range(3):
            for j in range(hash_arr[i]):
                nums[count]=i
                count+=1
        

        
        