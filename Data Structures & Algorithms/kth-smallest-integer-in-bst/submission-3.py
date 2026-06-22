# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1

        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            nonlocal res
            nonlocal k
            if k > 0:
                k -= 1
                res = curr.val

            dfs(curr.right)

        dfs(root)
        print(res)

        return res