#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-29 10:32:04
# File Name: rangeModule.py
# Description: 范围模块 
# LintCode: https://www.lintcode.com/problem/range-module/
#########################################################################
class Solution(object):

    def __init__(self):
        self.range = []

    def addRange(self, left, right):
        n = len(self.range)
        cur = 0

        for i in range(0, n):
            # 两个区间不相交
            if self.range[i][1] < left:
                cur += 1
            # 两个区间不相交
            elif self.range[i][0] > right:
                continue
            else:
                left = 

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """

obj = Solution()
# vim: set noexpandtab ts=4 sts=4 sw=4 :
