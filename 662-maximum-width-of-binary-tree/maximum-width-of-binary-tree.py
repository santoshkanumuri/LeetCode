# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        levels=[]
        queue= collections.deque([(root,1,0)])

        max_width=1

        while queue:
            lev=[]
            size=len(queue)
            for i in range(size):
                node,num,level = queue.popleft()

                if node:
                    lev.append(num)

                if node.left:
                    queue.append((node.left,2*num,level+1))
                
                if node.right:
                    queue.append((node.right,2*num+1,level+1))
            
                
            if len(lev)!=0:
                max_width=max(max_width,lev[-1]-lev[0]+1)
            levels.append(lev)
        
        print(levels)
        return max_width
        