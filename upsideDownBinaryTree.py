class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def upsideDownBinaryTree(self, root):
        # write your code here
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.right = None
        root.left = None
        return new_root
