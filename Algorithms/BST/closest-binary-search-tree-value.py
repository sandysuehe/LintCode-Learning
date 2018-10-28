#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: closest-binary-search-tree-value.py
# Description: Closest Binary Search Tree Value 
# LintCode: https://www.lintcode.com/problem/closest-binary-search-tree-value/ 
#########################################################################
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

