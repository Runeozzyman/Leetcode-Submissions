# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        values = []
        self.inOrderTraversal(root,values)
        return values [k-1]

    
    def inOrderTraversal(self,root,values):
        if not root:
            return

        self.inOrderTraversal(root.left, values)
        values.append(root.val)
        self.inOrderTraversal(root.right, values)