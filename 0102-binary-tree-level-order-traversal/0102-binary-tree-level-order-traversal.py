# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            q = []
            if root:
                q.append(root)
            res = []
            while q:
                temp = []
                for i in range(0, len(q)):
                    cur = q[0]
                    temp.append(cur.val)
                    del q[0]
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                res.append(temp)
            return res
        return bfs(root)
                    
            