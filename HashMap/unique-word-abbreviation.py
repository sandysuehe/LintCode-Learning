#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 18:24:33
# File Name: unique-word-abbreviation.py
# Description: unique-word-abbreviation 
# LintCode: https://www.lintcode.com/problem/unique-word-abbreviation/
#########################################################################
class ValidWordAbbr:
    def __init__(self, dictionary):
        self.word_map = {}
        self.abbr_map = {}

        for word in dictionary:
            self.word_map[word] = 1
            key = word[0] + str(len(word)-2) + word[-1]
            self.abbr_map[key] = self.abbr_map.get(key, 0) + 1

    def isUnique(self, word):
        if len(word) in (0, 1, 2):
            return True

        key = word[0] + str(len(word)-2) + word[-1]

        if word in self.word_map:
            if self.abbr_map[key] == 1:
                return True
            return False

        if key in self.abbr_map:
            if self.abbr_map[key] >= 1:
                return False
        return True


dictionary = [ "deer", "door", "cake", "card" ]
word = "cart"
word = "dear"
obj = ValidWordAbbr(dictionary)
print obj.isUnique(word)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
