# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left=head
        right=self.getmid(left)
        tmp=right.next
        right.next=None
        right=tmp

        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)

    def getmid(self,head):
        s,f=head,head.next
        while f and f.next:
            f=f.next.next
            s=s.next
        return s

    def merge(self,left,right):
        tail=dummy=ListNode(0)
        while left and right:
            if left.val<right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if left:
            tail.next=left
        if right:
            tail.next=right
        return dummy.next
    
