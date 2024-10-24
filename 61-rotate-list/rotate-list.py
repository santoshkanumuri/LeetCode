# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur=head
        n=0
        while cur:
            last=cur 
            cur=cur.next
            n+=1    
        r=k%n
        k=n-r
        if r==0:
            return head
        cur=head
        while k!=1:
            cur=cur.next
            k=k-1
        last.next=head
        p=cur.next
        cur.next=None
        
        return p
