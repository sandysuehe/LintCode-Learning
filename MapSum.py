#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: MapSum.py
# Description: 
#########################################################################
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.count = 0

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.key_set = set()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if len(key) == 0:
            return

        curNode = self.root

        for letter in key:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()

            curNode = curNode.children[letter]

            if key not in self.key_set:
                curNode.count += val
            else:
                curNode.count = val

        self.key_set.add(key)

    def startsWith(self, prefix):
        curNode = self.root
        for letter in prefix:
            if letter not in curNode.children:
                return None
            curNode = curNode.children[letter]
        return curNode

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.startsWith(prefix)
        if not node:
            return 0
        return node.count

# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print obj.sum("ap")
obj.insert("app", 2)
print obj.sum("ap")
# vim: set noexpandtab ts=4 sts=4 sw=4 :
