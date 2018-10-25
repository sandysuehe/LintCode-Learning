#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 18:08:20
# File Name: word-abbreviation.py
# Description: Word Abbreviation 
# LintCode: http://www.jiuzhang.com/solution/word-abbreviation/
#########################################################################
class Solution:
    def wordsAbbreviation(self, dict):
        # write your code here
        self.result = {}
        self.solve(dict, 0)
        return map(self.result.get, dict)
        
    
    def abbr(self, word, size):
        if len(word) - size <=3:
            return word
        return word[:size + 1] + str(len(word) - size -2) + word[-1]
        
    def solve(self, dict, size):
        abbr_dict = {}
        for word in dict:
            key = self.abbr(word, size)
            if key not in abbr_dict:
                abbr_dict[key] = [word]
            else:
                abbr_dict[key].append(word)
        for abbr in abbr_dict:
            word_list = abbr_dict[abbr]
            if len(word_list) == 1:
                self.result[word_list[0]] = abbr
            else:
                self.solve(word_list, size + 1)
            

obj = Solution()
dict = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
print obj.wordsAbbreviation(dict)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
