# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        res=[]
        levels=collections.defaultdict(list)
        queue = collections.deque([(root,0,0)])
        min_level=float('inf')
        max_level=float('-inf')

        while queue:
            node, row, col = queue.popleft()

            min_level=min(col,min_level)
            max_level=max(col,max_level)

            levels[col].append((node.val, row))

            if node.left:
                queue.append([node.left,row+1,col-1])
            
            if node.right:
                queue.append([node.right,row+1,col+1])


        for level in range(min_level,max_level+1):
            item=levels[level]
            item.sort(key=lambda x:(x[1],x[0]))

            item= [v for v,x in item]
            res.append(item)

        return res
