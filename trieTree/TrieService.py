#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 11:51:08
# File Name: TrieService.py
# Description: 
#########################################################################
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.top10 = []


class TrieService(object):
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, word, frequency):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()

            curNode = curNode.children[letter]
            curNode.top10.append(frequency)
            curNode.top10 = sorted(curNode.top10)[::-1]
            if len(curNode.top10) > 10:
                curNode.top10.pop()
        print curNode.top10

obj = TrieService()
obj.insert("abc", 2)
obj.insert("ac", 4)
obj.insert("ab", 9)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
