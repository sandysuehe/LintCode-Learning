#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: find-the-celebrity.py
# Description: find-the-celebrity 
# LintCode: https://www.lintcode.com/problem/find-the-celebrity/
#########################################################################
# 思路:
# 设定候选人ans为0，原理是先遍历一遍，
# 对于遍历到的人i，若候选人ans认识i，则将候选人ans设为i,
# 完成一遍遍历后，检测候选人ans是否真正是名人，
# 如果判断不是名人，则返回-1，如果并没有冲突，返回ans
#########################################################################
def findCelebrity(n):
    # Write your code here
    ans = 0;
    for i in range(n):
        if Celebrity.knows(ans, i):
            ans = i

    for i in range(n):
        if ans != i and (Celebrity.knows(ans, i) or not Celebrity.knows(i, ans)):
            return -1

    return ans
