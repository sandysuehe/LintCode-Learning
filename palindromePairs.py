#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 15:28:39
# File Name: palindromePairs.py
# Description: 
#########################################################################
def isPalindrome(word, left, right):
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def palindromePairs(words):
    res = set()
    hash_set = {}
    len_set = []

    for i in range(0, len(words)):
        # 建立word和index的映射hash_set
        hash_set[words[i]] = i
        # 保存出现过的单词长度集合set
        len_set.append(len(words[i]))
    len_set = sorted(len_set)

    for i in range(0, len(words)):
        temp = words[i]
        len_temp = len(words[i])
        reverse = ''.join(temp[j] for j in range(len(temp)-1, -1, -1))

        # 情况1：如果abc和cba为回文对
        if reverse in hash_set and hash_set[reverse] != i:
            res.add((i, hash_set[reverse]))

        # 情况2: 如果lls和sssll组成为回文
        num = len_set.index(len_temp)
        for j in range(0, num):
            len_other = len_set[j]
            if isPalindrome(reverse, 0, len_temp-len_other-1) and reverse[len_temp-len_other:] in hash_set:
                res.add((i, hash_set[reverse[len_temp-len_other:]]))
            if isPalindrome(reverse, len_other, len_temp-1) and reverse[0:len_other] in hash_set:
                res.add((hash_set[reverse[0:len_other]], i))
    return [list(item) for item in res]


words = ["bat", "tab", "cat"]
words = ["abcd", "dcba", "lls", "s", "sssll"]
print palindromePairs(words)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
