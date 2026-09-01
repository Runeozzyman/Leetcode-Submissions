# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        q = []

        def preorder(node):
            if not node:
                return
            q.append(node)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)

        if q:
            q.pop(0)
        while q:
            root.right = q.pop(0)
            root.left = None
            root = root.right