class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        for i in range(k):
            l=nums.pop(n-1)
            nums.insert(0,l)

           
        