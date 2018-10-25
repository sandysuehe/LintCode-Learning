#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 12:54:01
# File Name: longest-absolute-file-path.py
# Description: Longest Absolute File Path 
# LintCode: https://www.lintcode.com/problem/longest-absolute-file-path/
#########################################################################
def lengthLongestPath(input):
    res = 0
    n = len(input)
    level = 0
    hash_map = {0: 0}

    i = 0
    while i < n:
        j = i
        while i < n and input[i] not in ("\t", "\n"):
            i += 1

        if i >= n or input[i] == "\n": 
            name = input[j: i]
            if name.find(".") != -1:  # 遇到了文件
                res = max(res, hash_map.get(level, 0) + len(name))
                print "file: {0} level: {1} len: {2}, max_len: {3}".format(name, level, len(name), res) 
            else:     # 遇到了文件夹
                level += 1
                hash_map[level] = hash_map[level-1] + len(name)
                print "dir: {0} level: {1} len: {2}".format(name, level, len(name)) 
                print "\n", hash_map
            level = 0
        else:
            level += 1  # input[i] == "\t", level由"\t"的个数来统计
        i += 1
    return res

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print lengthLongestPath(input)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
