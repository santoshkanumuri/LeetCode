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
        nodes=[]
       
        for i in range(rot):
            diff=k
            for j in range(diff-1):
                right=right.next
                
            tmp=right.next
            new=self.reverse(left,tmp)
            nodes.append(new)
            left,right=tmp,tmp
            if tmp:
                print(tmp.val)
        tmp1=None
        for i,node in enumerate(nodes,start=0):
            while node.next:
                node=node.next
                tmp1=node
            if(i+1<len(nodes)):
                node.next=nodes[i+1]
        tmp1.next=tmp
        return nodes[0]
            
        return head


        
        