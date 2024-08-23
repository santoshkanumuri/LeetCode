class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ''' This program uses moore's algorithm to find the optimal solution for the problems which checks if the given number's
        frequency in the array is greater than n/2 and returns that element.

        intution:
            we initially take first element as target and increase count to check how many time that number appeared. if the number is appeared then we increase 
            count else if any other number appeared then we decrease the count. if we touch count to zero then we take the next element
            as target and continue our iteration until iterating the complete array.

            finally that algorithm states if a majority element exists in the array then this algorithm catches it, if not it will return a wrong element
            so make sure to check the count of output is greater than n/2 before returning it.



            in this given question they stated that element alays exist so i havent checked count for it.
        '''
        count=0
        for num in nums:
            if(count==0):
                target=num
            if(target==num):
                count+=1
            else:
                count-=1
                
        return target
