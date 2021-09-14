# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
​
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.curr = None
        
​
    def next(self) -> int:
        temp = self.inOrderSuccessor(self.root, self.curr)
        if temp != -1:
            self.curr = temp
            return self.curr.val
        return -1
​
    def hasNext(self) -> bool:
        if self.inOrderSuccessor(self.root, self.curr) != -1:
            return True
        return False
            
    
    def inOrderSuccessor(self, root, target):
        if root is None:
            return -1
        
        if not self.curr:
            return self.findMinNode(self.root)
        
        curr = self.root
        candidate = -1
        
        while curr:
            if curr == target:
                if not curr.right:
                    return candidate
                candidate = curr.right
                curr = curr.right
            elif curr.val > target.val:
                candidate = curr
                curr = curr.left
            else:
                curr = curr.right
                
        return candidate
    
    def findMinNode(self, root):
        if not root:
            return None
        
        if root.left:
            return self.findMinNode(root.left)
        
        return root
        
        
​
​
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
