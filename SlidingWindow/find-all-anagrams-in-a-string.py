#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 15:28:01
# File Name: find-all-anagrams-in-a-string.py
# Description: Find All Anagrams in a String 
# LintCode: https://www.lintcode.com/problem/find-all-anagrams-in-a-string/
#########################################################################
def findAnagrams(s, p):
    # write your code here
    ans = []
    if not s or len(s) == 0:
        return ans

    left = 0
    right = 0
    n = len(s)
    count = len(p)
    hash_map = {}

    for char in p:
        hash_map[char] = hash_map.get(char, 0) + 1 

    while right < n:
        if s[right] in hash_map:      # 如果右边界的字符已经在哈希表中了，说明该字符在p中有出现
            if hash_map[s[right]] > 0:
                count -= 1            # count自减1
            hash_map[s[right]] -= 1   # 哈希表中该字符个数自减1

        right += 1

        if count == 0:        # 如果此时count减为0了，说明p中的字符都匹配上了。
            ans.append(left)  # 左边界加入结果ans中

        if right - left == len(p):   # 如果此时right和left的差为p的长度，说明此时应该去掉最左边的一个字符
            if s[left] in hash_map:
                if hash_map[s[left]] >= 0: # 如果该字符在哈希表中的个数大于等于0，说明该字符是p中的字符
                    count += 1            # count自加1
                hash_map[s[left]] += 1   # 哈希表中该字符个数自加1
            left += 1
    return ans

s = "cbaebabacd"
p = "abc"
print findAnagrams(s, p)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
