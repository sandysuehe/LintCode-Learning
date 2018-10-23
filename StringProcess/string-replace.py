#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-23 18:47:47
# File Name: string-replace.py
# Description: String Replace
# LintCode: https://www.lintcode.com/problem/string-replace/
#########################################################################
def stringReplace(a, b, s):
    # Write your code here
    replace_lens = set()
    hash_map = {}

    for i in range(len(a)):
        replace_lens.add(len(a[i]))  # a数组中元素的长度集合replace_lens
        hash_map[a[i]] = i           # a数组中元素vs索引构建的哈希表hash_map
        
    replace_lens = sorted(replace_lens, reverse=True)

    ans = ""
    i = 0
    while i < len(s):
        flag = False
        for replace_len in replace_lens:
            j = i + replace_len
            if j > len(s):
                continue

            substr = s[i:j]
            if substr in a:
                ans += b[hash_map[substr]]
                flag = True 
                i = j
                break

        if not flag:
            ans += s[i]
            i += 1

    return ans

A = ["ab","aba"]
B = ["cc","ccc"]
S = "ababa"
print A, B, S
print stringReplace(A, B, S)

A = ["ab","aba"]
B = ["cc","ccc"]
S = "aaaaa"
print stringReplace(A, B, S)

A = ["cd","dab","ab"]
B = ["cc","aaa","dd"]
S = "cdab"
print stringReplace(A, B, S)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
