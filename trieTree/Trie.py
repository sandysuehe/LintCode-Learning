#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 11:35:03
# File Name: Trie.py
# Description: Implement Trie
#########################################################################
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.isWord = True

    def search(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                return False
            curNode = curNode.children[letter]
        return True

    def startsWith(self, prefix):
        curNode = self.root
        for letter in prefix:
            if letter not in curNode.children:
                return False
            curNode = curNode.children[letter]
        return True

obj = Trie()
obj.insert("lintcode")
print obj.search("lintcode")
print obj.startsWith("lint")
print obj.search("linterror")
print obj.startsWith("code")
# vim: set noexpandtab ts=4 sts=4 sw=4 :
