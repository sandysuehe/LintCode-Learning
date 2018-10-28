#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-23 12:16:56
# File Name: exits.py
# Description: 
#########################################################################
class Solution:

    def exist(self, board, word):
        if not board or len(board) == 0:
            return False
        self.m = len(board)
        self.n = len(board[0])

        visited = [[False] * self.n for i in range(self.m)]
        for i in range(0, self.m):
            for j in range(0, self.n):
                if self.dfs(board, word, 0, i, j, visited):
                    return True
        return False

    def dfs(self, board, word, index, x, y, visited):
        if index == len(word):
            return True

        if x < 0 or x >= self.m or y < 0 or y >= self.n or visited[x][y] or board[x][y] != word[index]:
            return False

        visited[x][y] = True
        res = self.dfs(board, word, index+1, x+1, y, visited) or self.dfs(board, word, index+1, x-1, y, visited) or self.dfs(board, word, index+1, x, y+1, visited) or self.dfs(board, word, index+1, x, y-1, visited)
        visited[x][y] = False
        return res

board = ["ABCE","SFCS","ADEE"]
word = "ABCCED"
board = ["ABCE","SFCS","ADEE"]
word = "ABCB"
board = ["ABCE","SFES","ADEE"]
word = "ABCESEEEFS"
obj = Solution()
print obj.exist(board, word)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
