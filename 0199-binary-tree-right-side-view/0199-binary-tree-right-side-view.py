# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            q = []
            if root:
                q.append(root) #Insert element in the queue
            res = []
            while(q):
                temp = []
                size = len(q)
                for i in range(0,size,1):
                    cur = q[0]
                    temp.append(cur.val)
                    del q[0]
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                res.append(temp[-1])
            
            return res
        
        return helper(root)