# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f:Node=head
        count:int=1
        c:int=1
        cur:Node=head
        if (f.next==None):
            if(n==1):
                return None
        
        while(f.next!=None):
            f=f.next
            count+=1
        pos=count-n
        if(pos==0):
            return head.next
        
        while(c!=pos and cur.next):
            c+=1
            cur=cur.next
        if(cur.next.next!=None):
            cur.next=cur.next.next
        else:
            cur.next=None
       
        return head
            

        


        
        