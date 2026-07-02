# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(curr):
            if not curr:
                return 0

            s = curr.val

            left = max(dfs(curr.left), 0)
            right = max(dfs(curr.right), 0)

            nonlocal res
            res = max(res, s + left + right)

            return s + max(left, right)

        dfs(root)

        return res