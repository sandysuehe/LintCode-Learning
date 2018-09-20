#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-27 19:31:48
# File Name: numMatchingSubseq.py
# Description: 
#########################################################################
def countSubsequences(source):
    n = len(source)
    ans = [0, 0, 0]
    for i in range(0, n):
        if source[i] == 'a':
            ans[0] = ans[0] * 2 + 1
        elif source[i] == 'b':
            ans[1] = ans[1] * 2 + ans[0]
        else:
            ans[2] = ans[2] * 2 + ans[1]
    return ans[-1]

print countSubsequences("abcabc")
# vim: set noexpandtab ts=4 sts=4 sw=4 :
