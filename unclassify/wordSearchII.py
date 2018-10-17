#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-23 10:20:58
# File Name: wordSearchII.py
# Description: 
#########################################################################
class Solution:
    def wordSearchII(self, board, words):
        if not board or len(board) == 0:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        self.m = len(board)
        self.n = len(board[0])

        visited = set()
        for i in range(0, self.m):
            for j in range(0, self.n):
                visited.add((i, j))
                self.dfs(board, i, j, trie.root.children.get(board[i][j]), visited, result)
                visited.remove((i, j))

        return list(result)

    def dfs(self, board, x, y, node, visited, result):
        if not node:
            return

        if node.isWord:
            result.add(node.word)

        if board[x][y] == "d":
            print board[x][y]

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for direct in dirs:
            dx = direct[0]
            dy = direct[1]
            new_x = x + dx
            new_y = y + dy

            if new_x >= 0 and new_x < self.m and new_y >=0 and new_y < self.n and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                self.dfs(board, new_x, new_y, node.children.get(board[new_x][new_y]), visited, result)
                visited.remove((new_x, new_y))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.isWord = True
        curNode.word = word

    def search(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                return None
            curNode = curNode.children[letter]
        return curNode

# board = ["doaf","agai","dcan"]
# words = ["dog","dad","dgdg","can","again"]
board = ["abce","sfcs","adee"]
words = ["as","ab","cf","da","ee","e","adee","eeda"]
obj = Solution()
print obj.wordSearchII(board, words)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
