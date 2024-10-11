# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur:ListNode=head
        prev:ListNode=None
        while(cur):
            temp=cur.next
            cur.next=prev
            prev=cur
            print(cur.val)
            cur=temp
            
        return prev
        
        
        