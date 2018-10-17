    class Solution:
        def closestValue(self, root, target):
            # write your code here
            low = root
            high = root

            while root:
                if root.val > target: 
                    high = root
                    root = root.left
                elif root.val < target:
                    low  = root
                    root = root.right
                else:
                    return root.val
                
            if abs(high.val-target) > abs(lower.val-target):
                return low.val
            return high.val

