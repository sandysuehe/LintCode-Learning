#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 18:04:57
# File Name: word-squares.py
# Description: 
#########################################################################
class Solution:
    def wordSquares(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        squares = []
        for word in words:
            self.dfs(trie, [word], squares)
        return squares

    def dfs(self, root, side, squares):
        n = len(side[0])
        m = len(side)

        if m == n:
            squares.append(list(side))
            return

        for row_index in range(m, n):
            prefix = "".join([side[i][row_index] for i in range(m)])
            print "prefix:::", prefix
            if not root.search(prefix):
                return

        prefix = ''.join([side[i][m] for i in range(m)])
        print "prefix:::", prefix, "word:::", root.getWordsAndPrefix(prefix)
        for word in root.getWordsAndPrefix(prefix):
            side.append(word)
            self.dfs(root, side, squares)
            side.pop()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.wordList = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
            curNode.wordList.append(word)
        curNode.isWord = True

    def search(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                return None
            curNode = curNode.children[letter]
        return curNode

    def getWordsAndPrefix(self, prefix):
        node = self.search(prefix)
        if not node:
            return []
        return node.wordList

    def isWord(self, word):
        node = self.search(prefix)
        if not node:
            return None
        return node.isWord

words = ["ball","area","lead","lady"]
obj = Solution()
print obj.wordSquares(words)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
