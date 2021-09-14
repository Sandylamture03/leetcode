class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left, right = 0, 0
        if not root:
            return 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        return 1 + max(left, right)
