# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        def bfs(root, level):
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            
            if root.left:
                bfs(root.left, level+1)
            if root.right:
                bfs(root.right, level+1)
            
        bfs(root, 0)
        return result
            
            