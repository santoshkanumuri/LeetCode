# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f=head
        if (f.next==None):
            if(n==1):
                return None
        count=1
        while(f.next!=None):
            f=f.next
            count+=1
        print(count)
        pos=count-n
        print(pos)
        if(pos==0):
            return head.next
        cur=head
        c=1
        while(c!=pos and cur.next):
            c+=1
            cur=cur.next
        if(cur.next.next!=None):
            cur.next=cur.next.next
        else:
            cur.next=None
       
        return head
            

        


        
        