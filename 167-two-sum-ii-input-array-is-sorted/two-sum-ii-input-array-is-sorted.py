class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low:int=0
        high:int=len(numbers)-1
        while(low<=high):
            total=numbers[low]+numbers[high]
            if(total<target):
                low+=1
            elif(total>target):
                high-=1
            else:
                return [low+1,high+1]


        