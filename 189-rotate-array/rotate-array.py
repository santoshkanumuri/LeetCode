class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        def reverse(l,r):
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1
        reverse(0,n-k-1)
        reverse(n-k,n-1)
        reverse(0,n-1)


           
        