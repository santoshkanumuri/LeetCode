# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        newlist=ListNode(val=0)
        v=newlist
        hm={}
        while cur:
            cval=cur.val
            if cur.next:
                if (cval!=cur.next.val and hm.get(cval,-1)!=0):
                    newlist.next=ListNode(cval)
                    newlist=newlist.next
            else:
                if hm.get(cval,-1)!=0:
                    newlist.next=ListNode(cval)
                    newlist=newlist.next
            cur=cur.next
            hm[cval]=0
        return v.next

        