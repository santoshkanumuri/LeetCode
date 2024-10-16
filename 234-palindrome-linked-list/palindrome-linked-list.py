# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head==None or head.next==None:
            return head
        else:
            newnode=self.reverse(head.next)
            front=head.next
            front.next=head
            head.next=None
            return newnode
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        new=self.reverse(slow)
        second=new
        first=head
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        
        return True

        

        
            

        