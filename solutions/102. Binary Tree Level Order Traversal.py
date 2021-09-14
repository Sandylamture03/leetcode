class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverseLayer(toTraverse): # return traversedList, nextQueue:
            output = []
            nextQueue = []
            for node in toTraverse:
                if node is not None:
                    output.append(node.val)
                    nextQueue.append(node.left)
                    nextQueue.append(node.right)
            
            return output, nextQueue
        
        output = []
        toTraverse = [root]
        
        while (toTraverse):
            temp, toTraverse = traverseLayer(toTraverse)
            
            if temp: output.append(temp)
            
        return output
