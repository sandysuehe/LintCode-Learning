#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-23 14:23:40
# File Name: TrieSerialize.py
# Description: 
#########################################################################
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()

class Solution:

    def serialize(self, root):
        if not root:
            return
        data = ""
        for key in root.children:
             value = root.children[key]
             data +=  key + self.serialize(value)
        return "<{}>".format(data)

    def deserialize(self, data):
        if not data or len(data) == 0:
            return None
        root = TrieNode()
        curNode = root
        path = []
        for letter in data:
           if letter == "<":
               path.append(curNode)
           elif letter == ">":
               path.pop()
           else:
               curNode = TrieNode()
               if len(path) == 0:
                   print letter, path
               path[-1].children[letter] = curNode
        return root
# vim: set noexpandtab ts=4 sts=4 sw=4 :
