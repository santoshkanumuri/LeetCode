# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=collections.deque([root])

        res=[]

        while queue:

            level_size= len(queue)
            level=[]
            for i in range(level_size):
                node=queue.popleft()
                if node:
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
            if not level==[]:
                res.append(level[-1])

        return res

        