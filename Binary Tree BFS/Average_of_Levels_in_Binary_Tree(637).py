# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        avgs = []
        queue = deque([root])

        while queue:
             level_sum = 0
             count = len(queue)

             for _ in range(count):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

             avgs.append(level_sum / count)
            
        return avgs