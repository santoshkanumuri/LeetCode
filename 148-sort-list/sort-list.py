# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        cur=head
        while cur:
            li.append(cur.val)
            cur=cur.next
        li.sort()
        cur=head
        i=0
        while cur:
            cur.val=li[i]
            cur=cur.next
            i+=1
        return head