# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        array = []
        def dfs(root):
            if root is None:
                return None
            array.append(root.val)
            dfs(root.right)
            dfs(root.left)
        dfs(root)
        array.sort()

        return array[k-1]