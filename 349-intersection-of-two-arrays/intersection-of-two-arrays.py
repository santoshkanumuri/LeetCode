class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=0
        r=0
        m=len(nums1)
        n=len(nums2)
        nums1.sort()
        nums2.sort()
        final=set()
        while(l<m and r<n):
            if(nums1[l]<nums2[r]):
                l+=1
            elif(nums1[l]>nums2[r]):
                r+=1
            else:
                final.add(nums1[l])
                l+=1
                r+=1
        print(final)
        return final


        