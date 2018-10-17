class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def flatten(self, root):
        # write your code here
        self.dfs(root)
        
    def dfs(self, root):
        if not root:
            return None

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        if right :
            return right
        
        if left:
            return left

        return root
