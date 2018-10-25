#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 15:06:25
# File Name: min-stack.py
# Description: min-stack
# LintCode: https://www.lintcode.com/problem/min-stack/
#########################################################################
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        number = self.stack.pop()
        if number == self.min_stack[-1]:
            self.min_stack.pop()
        return number

    """
    @return: An integer
    """
    def min(self):
        # write your code here
            return self.min_stack[-1]
# vim: set noexpandtab ts=4 sts=4 sw=4 :
