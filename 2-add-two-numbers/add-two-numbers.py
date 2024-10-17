# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f,s=l1,l2
        while f and s:
            f=f.next
            s=s.next
        if f:
            f,s=l2,l1
        else:
            f,s=l1,l2
        o=ListNode(0)
        out=o
        carry=0

        while s:
            if f:
                fval=f.val
                f=f.next
            else:
                fval=0
            t=carry+fval+s.val
            carry=t//10
            t=t%10
            out.next=ListNode(t)
            out=out.next
            s=s.next
        if carry:
            out.next=ListNode(carry)

        
        return o.next

            
            

        