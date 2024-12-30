# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root and not (root.left or root.right):
            return True

        if not (root.left or root.right):
            return False

        queue= collections.deque([root.left,root.right])

        while queue:

            level=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()

                if node:
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(None)

                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(None)
                else:
                    level.append(None)
                    
            if len(level)%2!=0:
                return False
            
            else:
                half=len(level)//2

                first=level[0:half]
                second=level[half:][::-1]
                print(first,second)
                if first != second:
                    return False
            
        return True
