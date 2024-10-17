# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        f=l1
        s=l2
        while f:
            f=f.next
            n1+=1
        while s:
            s=s.next
            n2+=1
        if n1>n2:
            return self.addTwoNumbers(l2,l1)
        
        f=l1
        s=l2
        o=ListNode(0)
        out=o
        carry=0

        while s:
            if f:
                fval=f.val
                f=f.next
            else:
                fval=0
            print(fval,s.val)
            t=carry+fval+s.val
            carry=0
            if t>9:
                carry=t//10
                t=t%10
            new=ListNode(t)
           
            out.next=new
            out=out.next
            s=s.next
        if carry:
            out.next=ListNode(carry)

        
        return o.next

            
            

        