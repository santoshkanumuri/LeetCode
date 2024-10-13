# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur=head
        n=0
        while cur:
            n+=1
            cur=cur.next
        cur=head
        print(n)
        num=0
        p=2**(n-1)
        print(p)
        while cur:
            num+=cur.val*p
            p=p//2
            cur=cur.next
        return num
        