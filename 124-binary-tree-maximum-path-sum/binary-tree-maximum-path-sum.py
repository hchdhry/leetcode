# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.output = float('-inf')  

        def dfs(node):
            if not node:
                return 0


            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            currentSum = node.val+left+right
            self.output = max(currentSum,self.output)

            return node.val + max(left, right)

        dfs(root)
        return self.output
