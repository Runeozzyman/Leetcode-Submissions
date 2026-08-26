class Solution(object):
    def sumNumbers(self, root):
        return self.sum(root, 0)
        
    def sum(self, root, currSum):
            if root is None:
                return 0
            
            currSum = currSum * 10 + root.val

            if root.left is None and root.right is None:
                return currSum
            
            return self.sum(root.left, currSum) + self.sum(root.right, currSum)