# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head,right):
        if head==right or head.next==right:
            return head
        else:
            newhead=self.reverse(head.next,right)
            f=head.next
            f.next=head
            head.next=right
            return newhead

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head
        l,r=head,head
        last=ListNode(0,head)
        p=last
        for i in range(left-1):
            last=l
            l=l.next
        for i in range(right-1):
            r=r.next
        k=self.reverse(l,r.next)
        print(k.val)
        last.next=k
        return p.next
        
       

        
        

        