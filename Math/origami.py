#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: origami.py
# Description: 折纸
# LintCode: https://www.lintcode.com/problem/origami
#########################################################################
def getString(n): 
    node_len = pow(2, n) - 1
    ans = []
    inorder(1, n, ans, True)
    return "".join(ans)

def inorder(i, n, ans, isLeft):
    if i == n:
        if isLeft:
            ans.append("0")
        else:
            ans.append("1")
        return
    else:
        inorder(i+1, n, ans, True)  # recursive left-child-tree 
        if isLeft:
            ans.append("0")
        else:
            ans.append("1")
        inorder(i+1, n, ans, False) # recursive right-child-tree 

n = 1
print getString(n)
n = 2
print getString(n)
n = 3
print getString(n)
n = 4
print getString(n)
