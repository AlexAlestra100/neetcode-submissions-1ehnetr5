# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(curr1, curr2):
            if not curr1 and not curr2:
                return None

            curr = TreeNode((curr1.val if curr1 else 0) + (curr2.val if curr2 else 0))

            curr.left = dfs((curr1.left if curr1 else None), (curr2.left if curr2 else None))
            curr.right = dfs((curr1.right if curr1 else None), (curr2.right if curr2 else None))

            return curr

        return dfs(root1, root2)