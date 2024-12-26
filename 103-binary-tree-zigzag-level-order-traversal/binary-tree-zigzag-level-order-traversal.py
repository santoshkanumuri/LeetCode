# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res=[]
        q = deque([root])
        f = 0

        while q:
            
            size=len(q)
            curr = []

            for i in range(size):
                node=q.popleft()
                if node:
                    curr.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if not f:
                res.append(curr)
                f+=1
            elif f:
                res.append(curr[::-1])
                f-=1

        return res


        