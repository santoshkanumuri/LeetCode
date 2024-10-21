# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur=head
        li1=l1=ListNode(0)
        li2=l2=ListNode(0)
        while cur:
            if cur.val<x:
                li1.next=ListNode(cur.val)
                li1=li1.next
            else:
                li2.next=ListNode(cur.val)
                li2=li2.next
            cur=cur.next
        
        li1.next=l2.next
        
        return l1.next
        