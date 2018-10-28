#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: group-anagrams.py
# Description: 错位词分组 group-anagrams 
# LintCode: https://www.lintcode.com/problem/group-anagrams/
#########################################################################
def groupAnagrams(strs):
    hash_map = {}
    ans = []

    for word in strs:
        key = "".join(sorted(word))

        if key not in hash_map:
            hash_map[key] = [word]
        else:
            hash_map[key].append(word)

    for key in hash_map:
        ans.append(hash_map[key])

    return ans

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(strs)
