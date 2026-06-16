# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, mVal):
            if not curr:
                return 0

            add = 1 if curr.val >= mVal else 0
            mVal = max(mVal, curr.val)

            left = dfs(curr.left, mVal)
            right = dfs(curr.right, mVal)

            return left + right + add

        return dfs(root, root.val - 1)