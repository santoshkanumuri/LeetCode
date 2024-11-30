# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q=collections.deque()
        node=root
        res=0
        q.append(node)
        while q:
            l=len(q)
            for i in range(l):
                it=q.popleft()
                if it:
                    q.append(it.left)
                    q.append(it.right)
            res+=1
        return res-1



        