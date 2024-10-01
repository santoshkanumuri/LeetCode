class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bs(arr,t,n):
            low:int=0
            high:int=n-1
            while(low<=high):
                mid:int=(low+high)//2
                if(arr[mid]==t):
                    return mid
                elif(arr[mid]>t):
                    high=mid-1
                else:
                    low=mid+1
            return -1

        n:int=len(numbers)
        for i in range(n):
            num2=bs(numbers,target-numbers[i],n)
            print(numbers[i],numbers[num2])
            if(num2!=-1 and num2!=i):
                if(i>num2):
                    return [num2+1,i+1]
                return [i+1,num2+1]


        