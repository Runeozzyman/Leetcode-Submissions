

#NOTE: This problem is intended to be solved with BFS but I find the DFS solution is much simpler and more elegant

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node, depth):
            if not node:
                return
            
            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root,0)

        return res 