# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,left,right):
        if left==right or left.next==right:
            return left
        else:
            newhead=self.reverse(left.next,right)
            front=left.next
            front.next=left
            left.next=None
            return newhead
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==1:
            return head
        n=0
        cur=head
        while cur:
            cur=cur.next
            n+=1
        rot=n//k
        rem=n%k
        left,right=head,head
        nodes,lefts=[],[]
        
        for i in range(rot):
            lefts.append(left)
            for j in range(k-1):
                right=right.next
            tmp=right.next
            new=self.reverse(left,tmp)
            nodes.append(new)
            left,right=tmp,tmp

        for i in range(rot-1):
            lefts[i].next=nodes[i+1]
        lefts[-1].next=tmp
        return nodes[0]
      
        