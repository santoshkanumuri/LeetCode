# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1,cur2=headA,headB
        while cur1 and cur2:
            cur1=cur1.next
            cur2=cur2.next
        node=None
       
        n=0
        if cur2:
            print(cur2.val)
            node1=headB
            node2=headA
            while cur2:
                n+=1
                cur2=cur2.next
        elif cur1:
            print(cur1.val)
            node1=headA
            node2=headB
            while cur1:
                n+=1
                cur1=cur1.next
        else:
            node1=headA
            node2=headB
        while n!=0:
            node1=node1.next
            print(node1.val)
            n-=1
        while node1 and node2:
            if(node1==node2):
                return node1
            node1=node1.next
            node2=node2.next
        
        
        


        
        

        