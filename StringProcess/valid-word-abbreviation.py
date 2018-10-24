#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 16:28:08
# File Name: valid-word-abbreviation.py
# Description: Valid Word Abbreviation
# LintCode: https://www.lintcode.com/problem/valid-word-abbreviation/
#########################################################################
def validWordAbbreviation(word, abbr):
    m = len(word)
    n = len(abbr)
    i = 0
    j = 0

    while i < m and j < n:
        if abbr[j].isdigit():
            if abbr[j] == "0":
                return False

            val = 0
            while j < n and abbr[j].isdigit():
                val = val*10 + int(abbr[j])
                j += 1
            i += val
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == m and j == n

s = "internationalization"
abbr = "i12iz4n"
print validWordAbbreviation(s, abbr)

s = "apple"
abbr = "a2e"
print validWordAbbreviation(s, abbr)
