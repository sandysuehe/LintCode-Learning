#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-07-26 18:04:32
# File Name: subsets.py
# Description: 子集
# LintCode: https://www.lintcode.com/problem/subsets/
#########################################################################
class Solution(object):
    def search(self, nums, temp_list, index):
        if len(nums) == index:
            print index, self.result
            self.result.append(temp_list)
            return
        self.search(nums, temp_list + [nums[index]], index+1)
        self.search(nums, temp_list, index+1)

    def subsets(self, nums):
        self.result = []
        self.search(sorted(nums), [], 0)
        return self.result

obj = Solution()
print obj.subsets([1,2,3])
# vim: set noexpandtab ts=4 sts=4 sw=4 :
