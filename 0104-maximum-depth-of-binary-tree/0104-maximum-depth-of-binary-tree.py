# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        


        def maxhi(root):
            if not root:
                return 0
            return max(maxhi(root.left),maxhi(root.right)) + 1
        
        return maxhi(root)