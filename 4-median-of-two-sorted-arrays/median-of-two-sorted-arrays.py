class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        if(n1>n2):
            return self.findMedianSortedArrays(nums2,nums1)

        low=0
        high=n1
        tmid=(n1+n2+1)//2
        while(low<=high):
            mid=(low+high)//2
            mid2=tmid-mid
            l1=(-10000000)
            l2=(-10000000)
            r1=(10000000)
            r2=(10000000)
            if(mid-1>=0):
                l1=nums1[mid-1]
            if(mid2-1>=0):
                l2=nums2[mid2-1]
            if(mid<n1):
                r1=nums1[mid]
            if(mid2<n2):
                r2=nums2[mid2]



            if(l1<=r2 and l2<=r1):
                if((n1+n2)%2==0):
                    return ((max(l1,l2)+min(r1,r2))/2)
                else:
                    return max(l1,l2)

            elif(l1>r2):
                high=mid-1
            elif(l2>r1):
                low=mid+1
        



        


