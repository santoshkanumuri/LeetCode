# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hm={}
        cur=head
        n=0
        while cur:
            if cur in hm:
                return cur
            else:
                hm[cur]=n
                n+=1
                cur=cur.next
        return None
