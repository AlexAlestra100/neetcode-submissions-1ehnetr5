# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        curr = TreeNode(preorder[0])

        leftInorder = inorder[:inorder.index(preorder[0])]
        rightInorder = inorder[inorder.index(preorder[0]) + 1:]

        leftPreorder = preorder[1:len(leftInorder) + 1]
        rightPreorder = preorder[len(leftInorder) + 1:]

        curr.left = self.buildTree(leftPreorder, leftInorder)

        curr.right = self.buildTree(rightPreorder, rightInorder)

        return curr