# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur=head
        num=0
        while cur:
            if not cur.val:
                num=num*2
            else:
                num=(num*2)+1
            cur=cur.next
        return num