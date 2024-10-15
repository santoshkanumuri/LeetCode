# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s,f=head,head
        s1,f1="",""
        while f and f.next:
            s1=s1+str(s.val)
            s=s.next
            f=f.next.next
        
        while s:
            f1=f1+str(s.val)
            s=s.next
        print(s1,f1)
        if (len(s1)!=len(f1)):
            f1=f1[1:]
        print(s1,f1)
        if(s1==f1[::-1]):
            return True
        return False
            
            

        