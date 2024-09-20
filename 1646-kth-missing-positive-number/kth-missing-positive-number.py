class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def bs(num,arr,n):
            low=0
            high=n-1
            while(low<=high):
                mid=(low+high)//2
                if(num==arr[mid]):
                    return True
                elif(num>arr[mid]):
                    low=mid+1
                else:
                    high=mid-1
            return False


        misd=[]
        n:int=len(arr)
        mx:int=max(arr)
        if(arr[n-1]==n):
            return n+k
        for num in range(1,mx+1):
            res=bs(num,arr,n)
            if(not res):
                misd.append(num)
        if(k<=len(misd)):
            return misd[k-1]
        else:
            return arr[-1]-len(misd)+k

            


        
        
        