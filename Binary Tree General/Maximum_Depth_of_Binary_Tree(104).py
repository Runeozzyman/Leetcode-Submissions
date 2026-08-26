class Solution(object):
    def maxDepth(self, root):
        
        if not root:
            return 0

        leftTree = self.maxDepth(root.left)
        rightTree = self.maxDepth(root.right)
        
        return max(leftTree, rightTree) + 1
