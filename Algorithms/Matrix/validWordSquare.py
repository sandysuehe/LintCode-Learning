#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 12:17:42
# File Name: validWordSquare.py
# Description: Valid Word Square 有效单词词广场
# LintCode: https://www.lintcode.com/problem/valid-word-square/
#########################################################################
def validWordSquare(words):
    m = len(words)
    n = len(words[0])
    if m != n:
        return False
    for i in range(0, m):
        col_word = ""
        for j in range(0, n):
            col_word += words[i][j]
        if col_word != words[i]: #判断行单词和列单词是否相等
            return False
    return True 

words = ["abcd", "bnrt", "crmy","dtye"]
print validWordSquare(words)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
