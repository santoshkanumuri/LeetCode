"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        hm={}
        while cur:
            hm[cur]=Node(cur.val)
            cur=cur.next
        new=Node(0)
        n=new
        cur=head
        while cur:
            new.next=hm[cur]
            new=new.next
            if cur.random:
                new.random=hm[cur.random]
            else:
                new.random=None
            cur=cur.next
        return n.next
            
        


        
        