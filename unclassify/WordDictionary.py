#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 14:34:39
# File Name: WordDictionary.py
# Description: 
#########################################################################
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.isWord = True

    def search(self, word):
        if not word:
            return False
        return self.dfs(word, self.root, 0)

    def dfs(self, word, root, start_index):
        for i in range(start_index, len(word)):
            if word[i] == ".":
                # 找到root下的所有的子结点
                for child_node in root.children:
                    if self.dfs(word, root.children[child_node], i+1):
                        return True
            if word[i] not in root.children:
                return False
            root = root.children[word[i]]
        return root.isWord

obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print obj.search("pad")
# print obj.search("bad")
# print obj.search(".ad")
# print obj.search("b..")
obj.addWord("ran")
obj.addWord("rune")
obj.addWord("runner")
obj.addWord("runs")
obj.addWord("add")
obj.addWord("adds")
obj.addWord("adder")
obj.addWord("addee")
print obj.search("r.n")
print obj.search("ru.n.e")
print obj.search("add")
print obj.search("add.")
print obj.search("adde.")
print obj.search(".an.")
print obj.search("...s")
print obj.search("....e.")
print obj.search(".......")
print obj.search("..n.r")
# vim: set noexpandtab ts=4 sts=4 sw=4 :
