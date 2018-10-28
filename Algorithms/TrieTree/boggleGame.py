#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-20 15:36:38
# File Name: boggleGame.py
# Description:  Boggle Game 拼字游戏 
# LintCode: https://www.lintcode.com/problem/boggle-game/
#########################################################################
class Solution(object):
    def boggleGame(self, board, words):
        if not board or not words:
            return 0
    
        self.m = len(board)
        self.n = len(board[0])
    
        trie = Trie()
        for word in words:
            trie.insert(word)

        visited = [[False] * self.n for i in range(self.m)]
        result = []
        self.dfs(board, trie.root, 0, 0, visited, result)

        return len(result)


    def dfs(self, board, node, x, y, visited, result):
        for i in range(x, self.m):
            for j in range(y, self.n):
                paths = []
                temp = []
                self.getAllPaths(board, node, i, j, paths, temp, visited)
                for path in paths:
                    word = ""
                    for path_node in path:
                        px = path_node[0]
                        py = path_node[1]
                        word += board[px][py]
                        visited[px][py] = True
                    temp.append(word)
                    print word

                #    if len(temp) > len(result):
                #        result = temp[:]
                #    print result

                    #self.dfs(board, node, i, j, visited, result)
                    #temp.pop()
                    #for path_node in path:
                    #    visited[path_node[0]][path_node[1]] = False
            #y = 0
                    

    def getAllPaths(self, board, node, x, y, paths, temp, visited):
        if x < 0 or x >= self.m or y < 0 or y >= self.n or board[x][y] not in node.children or visited[x][y]:
            return

        curNode = node.children[board[x][y]]
        if curNode.isWord:
            temp.append((x, y))
            paths.append(temp[:])
            temp.pop()
            return
        
        visited[x][y] = True

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for direct in dirs:
            dx = direct[0]
            dy = direct[1]
            new_x = x + dx
            new_y = y + dy

            temp.append((x, y))
            self.getAllPaths(board, curNode, new_x, new_y, paths, temp, visited)
            temp.pop()

        visited[x][y] = False
        return paths

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

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


board = [['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i']]

words = ["abc", "cfi", "beh", "defi", "gh"]

board = ["abcdefg","huyuyww","ghihjui","wuiiuww"]
words = {"efg","defi","gh","iuw","ww","iw","ghih","dasf","aaa"}

obj = Solution()
print obj.boggleGame(board, words)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
