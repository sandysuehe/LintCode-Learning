#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 15:28:39
# File Name: palindromePairs.py
# Description: 
#########################################################################
def isPalindrome(word):
    size = len(word)
    for x in range(size/2):
        if word[x] != word[size-x-1]:
            return False
    return True
    
def palindromePairs(words):
    # Write your code here
    hash_set = {}
    res = set()
    
    for i in range(0, len(words)):
        hash_set[words[i]] = i
    
    for word in hash_set:
        index = hash_set[word]
        reword = word[::-1]

        if word != "" and "" in hash_set and isPalindrome(word):
            res.add((index, hash_set[""]))
            res.add((hash_set[""], index))

        if reword in hash_set and hash_set[reword] != index:
            res.add((index, hash_set[reword]))
            res.add((hash_set[reword], index))
            
        for x in range(1, len(word)):
            left = word[:x]
            right = word[x:]
            releft = left[::-1]
            reright = right[::-1]
            if isPalindrome(left) and reright in hash_set:
                res.add((hash_set[reright], index))
            if isPalindrome(right) and releft in hash_set:
                res.add((index, hash_set[releft]))
    
    return list(res)

# words = ["bat", "tab", "cat"]
# words = ["abcd", "dcba", "lls", "s", "sssll"]
words = ["abcd","dcba","lls","s","sssll",""]
print palindromePairs(words)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
