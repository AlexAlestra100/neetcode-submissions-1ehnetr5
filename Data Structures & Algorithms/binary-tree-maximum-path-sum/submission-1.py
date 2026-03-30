# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        rootSum = float('-inf')

        def dfs(curr):
            nonlocal rootSum
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            largest = max(leftMax, rightMax)

            currSum = curr.val + largest

            rootSum = max(rootSum, curr.val + leftMax + rightMax)
            
            return currSum

        dfs(root)

        return rootSum