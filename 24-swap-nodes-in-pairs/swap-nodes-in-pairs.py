# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur=head
        while cur and cur.next:
            cur.val,cur.next.val=cur.next.val,cur.val
            cur=cur.next.next
        return head
        