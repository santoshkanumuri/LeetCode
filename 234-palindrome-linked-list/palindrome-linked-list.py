# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=head
        arr=[]
        while s:
            arr.append(s.val)
            s=s.next
        s=head
        while s:
            c=arr.pop(-1)
            if(c!=s.val):
                return False
            s=s.next
        return True
        
            

        