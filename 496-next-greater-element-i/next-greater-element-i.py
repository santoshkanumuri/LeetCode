class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        stack=[]
        li=[]
        for num in nums2:
            while stack and stack[-1]<num:
                top=stack.pop()
                hm[top]=num
            stack.append(num)
        while stack:
            top=stack.pop()
            hm[top]=-1
        for num in nums1:
            li.append(hm[num])
        return li

        