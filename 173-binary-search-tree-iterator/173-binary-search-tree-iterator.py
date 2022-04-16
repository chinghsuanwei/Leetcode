# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # s: 7 3
    # s: 7
    # s: 15 9
    # s: 15
    # s: 20
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left
        
        
    
    def next(self):
        
        
        root = self.stack.pop(-1)
        
        
        val = root.val
        
        root = root.right
        
        #have right 
        if root:
            #track left
            while root:
                self.stack.append(root)
                root = root.left
        
        
        
        return val

    def hasNext(self) -> bool:
        
        
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()