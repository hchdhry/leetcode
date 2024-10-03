# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
                return 0
        def dfs(root,CurrentHighest):
            if not root:
                return 0

            good_count = 1 if root.val >= CurrentHighest else 0
            CurrentHighest = max(CurrentHighest, root.val)

            good_count += dfs(root.left, CurrentHighest)
            good_count += dfs(root.right, CurrentHighest)

            return good_count
    
        return dfs(root, root.val)
                
            



