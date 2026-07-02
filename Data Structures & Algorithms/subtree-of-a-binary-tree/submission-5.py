# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSametree(self, curr, subCurr):
        if not curr and not subCurr:
            return True
        
        if curr and subCurr and curr.val == subCurr.val:
            if self.isSametree(curr.left, subCurr.left) and self.isSametree(curr.right, subCurr.right):
                return True

        return False
          
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot:
            if self.isSametree(root, subRoot):
                return True

            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return False