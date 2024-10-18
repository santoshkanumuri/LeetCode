# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hm={}
        cur1=headA
        cur2=headB
        while cur1:
            hm[cur1]=1
            cur1=cur1.next
        while cur2:
            if cur2 in hm:
                return cur2
            else:
                hm[cur2]=1
            cur2=cur2.next
        return None
        