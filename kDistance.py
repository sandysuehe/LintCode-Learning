#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-22 16:52:31
# File Name: kDistance.py
# Description: 
#########################################################################
class Solution:

    def kDistance(self, words, target, k):
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result = []
        n = len(target)
        dp = [i for i in range(len(target)+1)]

        self.dfs(dp, trie.root, n)
        if target == "" and "" in words:
            self.result.append("")
        return self.result

    def dfs(self, dp, node, n):
        if node.string and dp[n] <= k:
            self.result.append(node.string)

        cur = [0 for i in range(n+1)]
        cur[0] = dp[0] + 1
        
        letter_set = set(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        for letter in letter_set:
            if letter in node.children:
                for i in range(1, n+1):
                    if letter == target[i-1]:
                        cur[i] = dp[i-1]
                    else:
                        cur[i] = min(dp[i-1], dp[i], cur[i-1]) + 1
                self.dfs(cur, node.children[letter], n)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.string = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.string = word

words = ["abc","abd","abcd","adc"]
target = "ac"
k = 1
words = ["a","b","ba","babbab", ""]
target = ""
k = 5
obj = Solution()
print obj.kDistance(words, target, k)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
